import schedule
import tweepy

import credentials
from domain.trend import Trend
from provider import Provider


class TrendsProvider(Provider):
    _SCHEDULE_MINUTES = 10

    def __init__(self, woeid, formatter):
        super(TrendsProvider, self).__init__()
        self.api = self._create_api()
        self.woeid = woeid
        self.formatter = formatter

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
