import tweepy
import schedule

import credentials
from domain.trends.trend import Trend
from formatter.trends_formatter import TrendsFormatter

from provider import Provider


class TrendsProvider(Provider):
    _SCHEDULE_MINUTES = 15

    def __init__(self, woeid):
        super(TrendsProvider, self).__init__()
        self.formatter = TrendsFormatter()
        self.api = self._create_api()
        self.woeid = woeid

    def _create_api(self):
        auth = tweepy.OAuthHandler(credentials.twitter['consumer_key'], credentials.twitter['consumer_secret'])
        auth.set_access_token(credentials.twitter['access_token'], credentials.twitter['access_token_secret'])
        return tweepy.API(auth)

    def initialize(self):
        self._get_trends()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._get_trends)

    def _get_trends(self):
        result = self.api.trends_place(self.woeid)
        self.data = map(lambda json: Trend(json), result[0]['trends'])
