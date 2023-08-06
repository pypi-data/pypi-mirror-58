from __future__ import absolute_import, print_function, unicode_literals

import json
import sys
import time
from datetime import datetime, timedelta

import pandas as pd
from httpx.client import Client
from httpx.config import DEFAULT_TIMEOUT_CONFIG
from httpx.exceptions import HTTPError, ProxyError
from pandas.io.json._normalize import nested_to_record
from pytrendsasync import exceptions
import logging
import asyncio
from tenacity import AsyncRetrying
from tenacity.stop import stop_after_attempt
from tenacity.retry import retry_if_exception_type, retry_if_exception
from tenacity.wait import wait_exponential
from urllib.parse import quote

log = logging.getLogger(__name__)


class TrendReq(object):
    """
    Google Trends API
    """
    GET_METHOD = 'get'
    POST_METHOD = 'post'
    GENERAL_URL = 'https://trends.google.com/trends/api/explore'
    INTEREST_OVER_TIME_URL = 'https://trends.google.com/trends/api/widgetdata/multiline'
    INTEREST_BY_REGION_URL = 'https://trends.google.com/trends/api/widgetdata/comparedgeo'
    RELATED_QUERIES_URL = 'https://trends.google.com/trends/api/widgetdata/relatedsearches'
    TRENDING_SEARCHES_URL = 'https://trends.google.com/trends/hottrends/visualize/internal/data'
    TOP_CHARTS_URL = 'https://trends.google.com/trends/api/topcharts'
    SUGGESTIONS_URL = 'https://trends.google.com/trends/api/autocomplete/'
    CATEGORIES_URL = 'https://trends.google.com/trends/api/explore/pickers/category'
    TODAY_SEARCHES_URL = 'https://trends.google.com/trends/api/dailytrends'

    def __init__(self, hl='en-US', tz=360, geo='', timeout=DEFAULT_TIMEOUT_CONFIG,
                 proxies=[], retries=0, backoff_factor=0):
        """
        Initialize default values for params
        """
        # google rate limit
        self.google_rl = 'You have reached your quota limit. Please try again later.'

        # set user defined options used globally
        self.tz = tz
        self.hl = hl
        self.geo = geo
        self.kw_list = list()
        self.timeout = timeout
        self.proxies = proxies.copy()  # add a proxy option
        self.blacklisted_proxies = []
        self._rate_limited_proxies = []
        self.proxy_index = 0
        self.cookies = None

        # intialize widget payloads
        self.token_payload = dict()
        self.interest_over_time_widget = dict()
        self.interest_by_region_widget = dict()
        self.related_topics_widget_list = list()
        self.related_queries_widget_list = list()

        self.backoff_factor = backoff_factor
        self.retries = retries
        self._retry_config = dict(
            wait=wait_exponential(multiplier=self.backoff_factor), 
            stop=stop_after_attempt(self.retries),
            reraise=True
        )
        
    def _get_proxy(self):
        """
        Gets the currently set proxy. Returns None if no proxies.

        Returns:
            dict{str, str} -- A dict containing the protocol and url of a proxy
        """ 
        proxy = None
        if len(self.proxies) > 0:
            proxy = self.proxies[self.proxy_index]
            proxy = {'all': self.proxies[self.proxy_index]}
        return proxy
    
    def _iterate_proxy(self):
        """
        Iterates what proxy will be used for the next request.
        """
        if self.proxy_index < (len(self.proxies) - 1):
            self.proxy_index += 1
        else:
            self.proxy_index = 0

    async def _send_req(self, url, method=GET_METHOD, **kwargs):
        """
        Sends a request to the specified URL.
        
        Arguments:
            url {str} -- Url to send request to.
        
        Keyword Arguments:
            method {str} -- Method to use (part of httpx.client.Client) (default: {GET_METHOD})
        
        Raises:
            ResponseError: Raised if a non-200 response code it returned.
        
        Returns:
            Response -- A response object containing the requested information.
        """        
        proxy = self._get_proxy()
        async with Client(proxies=proxy) as c:
            req = getattr(c, method)
            response = await req(url, **kwargs)
        if not str(response.status_code).startswith('2'):
            raise exceptions.ResponseError(
                'The request failed: Google returned a '
                'response with code {0}.'.format(response.status_code),
                response=response)
        return response

    async def GetGoogleCookie(self):
        """
        Gets google cookie (used for each and every proxy)
        Blacklist proxies on error.
        """
        def retry_if_proxies_remaining(ex):
            should_retry = True
            if isinstance(ex, ProxyError) and ex.response.status_code == 429:
                logging.info((f"Proxy {self.proxies[self.proxy_index]} responded with 429."
                               " Will retry request with another proxy."))
                self._rate_limited_proxies.append(self.proxies[self.proxy_index])
                del self.proxies[self.proxy_index]
            elif len(self.proxies) > 0:
                logging.error((f"Proxy {self.proxies[self.proxy_index]} caused {str(ex)}."
                                " Blacklisting proxy and will retry request with another."))
                self.blacklisted_proxies.append(self.proxies[self.proxy_index])
                del self.proxies[self.proxy_index]
            else:
                should_retry = False
            self._iterate_proxy()
            return should_retry
        
        cfg = self._retry_config
        if len(self.proxies) > 0:
            cfg = dict(
                retry=retry_if_exception(retry_if_proxies_remaining), 
                reraise=cfg.get('reraise', True)
            )
        try:
            retryer = AsyncRetrying(**cfg)
            resp = await retryer.call(
                self._send_req, 'https://trends.google.com/?geo={geo}'.format(
                    geo=self.hl[-2:]), timeout=self.timeout)
        finally:
            self.proxies.extend(self._rate_limited_proxies)
            self._rate_limited_proxies.clear()
        
        cookies = resp.cookies.items()
        return dict(filter(lambda i: i[0] == 'NID', cookies))

    async def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        """Send a request to Google and return the JSON response as a Python object
        :param url: the url to which the request will be sent
        :param method: the HTTP method ('get' or 'post')
        :param trim_chars: how many characters should be trimmed off the beginning of the content of the response
            before this is passed to the JSON parser
        :param kwargs: any extra key arguments passed to the request builder (usually query parameters or data)
        :return:
        """
        if self.cookies is None or len(self.proxies) > 0:
            self.cookies = await self.GetGoogleCookie()

        retryer = AsyncRetrying(**self._retry_config)
        response = await retryer.call(
            self._send_req, url, method=method, timeout=self.timeout, 
            cookies=self.cookies, headers={'accept-language': self.hl}, **kwargs)
        # check if the response contains json and throw an exception otherwise
        # Google mostly sends 'application/json' in the Content-Type header,
        # but occasionally it sends 'application/javascript
        # and sometimes even 'text/javascript
        if response.status_code == 200 and 'application/json' in \
                response.headers['Content-Type'] or \
                'application/javascript' in response.headers['Content-Type'] or \
                'text/javascript' in response.headers['Content-Type']:
            # trim initial characters
            # some responses start with garbage characters, like ")]}',"
            # these have to be cleaned before being passed to the json parser
            content = response.text[trim_chars:]
            # parse json
            self._iterate_proxy()
            return json.loads(content)
        else:
            # error
            raise exceptions.ResponseError(
                'The request failed: Google returned a '
                'response with code {0}.'.format(response.status_code),
                response=response)

    async def build_payload(self, kw_list, cat=0, timeframe='today 5-y', geo='',
                      gprop=''):
        """Create the payload for related queries, interest over time and interest by region"""
        self.kw_list = kw_list
        self.geo = geo or self.geo
        self.token_payload = {
            'hl': self.hl,
            'tz': self.tz,
            'req': {'comparisonItem': [], 'category': cat, 'property': gprop}
        }

        # build out json for each keyword
        for kw in self.kw_list:
            keyword_payload = {'keyword': kw, 'time': timeframe,
                               'geo': self.geo}
            self.token_payload['req']['comparisonItem'].append(keyword_payload)
        # requests will mangle this if it is not a string
        self.token_payload['req'] = json.dumps(self.token_payload['req'])
        # get tokens
        await self._tokens()

    async def _tokens(self):
        """Makes request to Google to get API tokens for interest over time, interest by region and related queries"""
        # make the request and parse the returned json
        resp = await self._get_data(
            url=TrendReq.GENERAL_URL,
            method=TrendReq.GET_METHOD,
            params=self.token_payload,
            trim_chars=4
        )
        widget_dict = resp['widgets']
        # order of the json matters...
        first_region_token = True
        # clear self.related_queries_widget_list and self.related_topics_widget_list
        # of old keywords'widgets
        self.related_queries_widget_list[:] = []
        self.related_topics_widget_list[:] = []
        # assign requests
        for widget in widget_dict:
            if widget['id'] == 'TIMESERIES':
                self.interest_over_time_widget = widget
            if widget['id'] == 'GEO_MAP' and first_region_token:
                self.interest_by_region_widget = widget
                first_region_token = False
            # response for each term, put into a list
            if 'RELATED_TOPICS' in widget['id']:
                self.related_topics_widget_list.append(widget)
            if 'RELATED_QUERIES' in widget['id']:
                self.related_queries_widget_list.append(widget)
        return

    async def interest_over_time(self):
        """Request data from Google's Interest Over Time section and return a dataframe"""

        over_time_payload = {
            # convert to string as requests will mangle
            'req': json.dumps(self.interest_over_time_widget['request']),
            'token': self.interest_over_time_widget['token'],
            'tz': self.tz
        }

        # make the request and parse the returned json
        req_json = await self._get_data(
            url=TrendReq.INTEREST_OVER_TIME_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=over_time_payload,
        )
        
        df = pd.DataFrame(req_json['default']['timelineData'])
        if (df.empty):
            return df

        df['date'] = pd.to_datetime(df['time'].astype(dtype='float64'),
                                    unit='s')
        df = df.set_index(['date']).sort_index()
        # split list columns into seperate ones, remove brackets and split on comma
        result_df = df['value'].apply(lambda x: pd.Series(
            str(x).replace('[', '').replace(']', '').split(',')))
        # rename each column with its search term, relying on order that google provides...
        for idx, kw in enumerate(self.kw_list):
            # there is currently a bug with assigning columns that may be
            # parsed as a date in pandas: use explicit insert column method
            result_df.insert(len(result_df.columns), kw,
                             result_df[idx].astype('int'))
            del result_df[idx]

        if 'isPartial' in df:
            # make other dataframe from isPartial key data
            # split list columns into seperate ones, remove brackets and split on comma
            df = df.fillna(False)
            result_df2 = df['isPartial'].apply(lambda x: pd.Series(
                str(x).replace('[', '').replace(']', '').split(',')))
            result_df2.columns = ['isPartial']
            # concatenate the two dataframes
            final = pd.concat([result_df, result_df2], axis=1)
        else:
            final = result_df
            final['isPartial'] = False
        
        return final

    async def interest_by_region(self, resolution='COUNTRY', inc_low_vol=False,
                           inc_geo_code=False):
        """Request data from Google's Interest by Region section and return a dataframe"""

        # make the request
        region_payload = dict()
        if self.geo == '':
            self.interest_by_region_widget['request'][
                'resolution'] = resolution
        elif self.geo == 'US' and resolution in ['DMA', 'CITY', 'REGION']:
            self.interest_by_region_widget['request'][
                'resolution'] = resolution

        self.interest_by_region_widget['request'][
            'includeLowSearchVolumeGeos'] = inc_low_vol

        # convert to string as requests will mangle
        region_payload['req'] = json.dumps(
            self.interest_by_region_widget['request'])
        region_payload['token'] = self.interest_by_region_widget['token']
        region_payload['tz'] = self.tz

        # parse returned json
        req_json = await self._get_data(
            url=TrendReq.INTEREST_BY_REGION_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=region_payload,
        )
        df = pd.DataFrame(req_json['default']['geoMapData'])
        if (df.empty):
            return df

        # rename the column with the search keyword
        df = df[['geoName', 'geoCode', 'value']].set_index(
            ['geoName']).sort_index()
        # split list columns into seperate ones, remove brackets and split on comma
        result_df = df['value'].apply(lambda x: pd.Series(
            str(x).replace('[', '').replace(']', '').split(',')))
        if inc_geo_code:
            result_df['geoCode'] = df['geoCode']

        # rename each column with its search term
        for idx, kw in enumerate(self.kw_list):
            result_df[kw] = result_df[idx].astype('int')
            del result_df[idx]

        return result_df

    async def related_topics(self):
        """Request data from Google's Related Topics section and return a dictionary of dataframes

        If no top and/or rising related topics are found, the value for the key "top" and/or "rising" will be None
        """

        # make the request
        related_payload = dict()
        result_dict = dict()
        for request_json in self.related_topics_widget_list:
            # ensure we know which keyword we are looking at rather than relying on order
            kw = request_json['request']['restriction'][
                'complexKeywordsRestriction']['keyword'][0]['value']
            # convert to string as requests will mangle
            related_payload['req'] = json.dumps(request_json['request'])
            related_payload['token'] = request_json['token']
            related_payload['tz'] = self.tz

            # parse the returned json
            req_json = await self._get_data(
                url=TrendReq.RELATED_QUERIES_URL,
                method=TrendReq.GET_METHOD,
                trim_chars=5,
                params=related_payload,
            )

            # top topics
            try:
                top_list = req_json['default']['rankedList'][0][
                    'rankedKeyword']
                df_top = pd.DataFrame(
                    [nested_to_record(d, sep='_') for d in top_list])
            except KeyError:
                # in case no top topics are found, the lines above will throw a KeyError
                df_top = None

            # rising topics
            try:
                rising_list = req_json['default']['rankedList'][1][
                    'rankedKeyword']
                df_rising = pd.DataFrame(
                    [nested_to_record(d, sep='_') for d in rising_list])
            except KeyError:
                # in case no rising topics are found, the lines above will throw a KeyError
                df_rising = None

            result_dict[kw] = {'rising': df_rising, 'top': df_top}
        return result_dict

    async def related_queries(self):
        """Request data from Google's Related Queries section and return a dictionary of dataframes

        If no top and/or rising related queries are found, the value for the key "top" and/or "rising" will be None
        """

        # make the request
        related_payload = dict()
        result_dict = dict()
        for request_json in self.related_queries_widget_list:
            # ensure we know which keyword we are looking at rather than relying on order
            kw = request_json['request']['restriction'][
                'complexKeywordsRestriction']['keyword'][0]['value']
            # convert to string as requests will mangle
            related_payload['req'] = json.dumps(request_json['request'])
            related_payload['token'] = request_json['token']
            related_payload['tz'] = self.tz

            # parse the returned json
            req_json = await self._get_data(
                url=TrendReq.RELATED_QUERIES_URL,
                method=TrendReq.GET_METHOD,
                trim_chars=5,
                params=related_payload,
            )

            # top queries
            try:
                top_df = pd.DataFrame(
                    req_json['default']['rankedList'][0]['rankedKeyword'])
                top_df = top_df[['query', 'value']]
            except KeyError:
                # in case no top queries are found, the lines above will throw a KeyError
                top_df = None

            # rising queries
            try:
                rising_df = pd.DataFrame(
                    req_json['default']['rankedList'][1]['rankedKeyword'])
                rising_df = rising_df[['query', 'value']]
            except KeyError:
                # in case no rising queries are found, the lines above will throw a KeyError
                rising_df = None

            result_dict[kw] = {'top': top_df, 'rising': rising_df}
        return result_dict

    async def trending_searches(self, pn='united_states'):
        """Request data from Google's Hot Searches section and return a dataframe"""

        # make the request
        # forms become obsolute due to the new TRENDING_SEACHES_URL
        # forms = {'ajax': 1, 'pn': pn, 'htd': '', 'htv': 'l'}
        req_json = await self._get_data(
            url=TrendReq.TRENDING_SEARCHES_URL,
            method=TrendReq.GET_METHOD
        )
        req_json = req_json[pn]
        result_df = pd.DataFrame(req_json)
        return result_df

    async def today_searches(self, pn='US'):
        """Request data from Google Daily Trends section and returns a dataframe"""
        forms = {'ns': 15, 'geo': pn, 'tz': '-180', 'hl': 'en-US'}
        req_json = await self._get_data(
            url=TrendReq.TODAY_SEARCHES_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=forms
        )
        trending_searches = req_json['default']['trendingSearchesDays'][0]['trendingSearches']
        result_df = pd.DataFrame()
        # parse the returned json
        sub_df = pd.DataFrame()
        for trend in trending_searches:
            sub_df = sub_df.append(trend['title'], ignore_index=True)
        result_df = pd.concat([result_df, sub_df])
        return result_df.iloc[:, -1]

    async def top_charts(self, date, hl='en-US', tz=300, geo='GLOBAL'):
        """Request data from Google's Top Charts section and return a dataframe"""
        # create the payload
        chart_payload = {'hl': hl, 'tz': tz, 'date': date, 'geo': geo,
                         'isMobile': False}

        # make the request and parse the returned json
        req_json = await self._get_data(
            url=TrendReq.TOP_CHARTS_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=chart_payload,
        )
        top_chart_items = req_json['topCharts'][0]['listItems']
        df = pd.DataFrame(top_chart_items)
        return df

    async def suggestions(self, keyword):
        """Request data from Google's Keyword Suggestion dropdown and return a dictionary"""

        # make the request
        kw_param = quote(keyword)
        parameters = {'hl': self.hl}

        req_json = await self._get_data(
            url=TrendReq.SUGGESTIONS_URL + kw_param,
            params=parameters,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
        )
        suggestions = req_json['default']['topics']
        return suggestions

    async def categories(self):
        """Request available categories data from Google's API and return a dictionary"""

        params = {'hl': self.hl}

        req_json = await self._get_data(
            url=TrendReq.CATEGORIES_URL,
            params=params,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
        )
        return req_json

    async def get_historical_interest(self, keywords, year_start=2018, month_start=1,
                                day_start=1, hour_start=0, year_end=2018,
                                month_end=2, day_end=1, hour_end=0, cat=0,
                                geo='', gprop='', sleep=0):
        """Gets historical hourly data for interest by chunking requests to 1 week at a time (which is what Google allows)"""

        # construct datetime obejcts - raises ValueError if invalid parameters
        initial_start_date = start_date = datetime(year_start, month_start,
                                                   day_start, hour_start)
        end_date = datetime(year_end, month_end, day_end, hour_end)

        # the timeframe has to be in 1 week intervals or Google will reject it
        delta = timedelta(days=7)

        df = pd.DataFrame()

        date_iterator = start_date
        date_iterator += delta

        while True:
            # format date to comply with API call

            start_date_str = start_date.strftime('%Y-%m-%dT%H')
            date_iterator_str = date_iterator.strftime('%Y-%m-%dT%H')

            tf = start_date_str + ' ' + date_iterator_str

            try:
                await self.build_payload(keywords, cat, tf, geo, gprop)
                week_df = await self.interest_over_time()
                df = df.append(week_df)
            except Exception as e:
                print(e)
                pass

            start_date += delta
            date_iterator += delta

            if (date_iterator > end_date):
                # Run for 7 more days to get remaining data that would have been truncated if we stopped now
                # This is needed because google requires 7 days yet we may end up with a week result less than a full week
                start_date_str = start_date.strftime('%Y-%m-%dT%H')
                date_iterator_str = date_iterator.strftime('%Y-%m-%dT%H')

                tf = start_date_str + ' ' + date_iterator_str

                try:
                    await self.build_payload(keywords, cat, tf, geo, gprop)
                    week_df = await self.interest_over_time()
                    df = df.append(week_df)
                except Exception as e:
                    print(e)
                    pass
                break

            # just in case you are rate-limited by Google. Recommended is 60 if you are.
            if sleep > 0:
                time.sleep(sleep)

        # Return the dataframe with results from our timeframe
        return df.loc[initial_start_date:end_date]
        