import time

import logging

import thread

from domain.crypto.coin_id import CoinId
from provider.crypto_provider import CryptoProvider
from provider.date_provider import DateProvider
from provider.rss_provider import RSSProvider
from provider.trends_provider import TrendsProvider
from provider.weather_provider import WeatherProvider


class ScrollerPresenter(object):
    logger = logging.getLogger()
    pointer = -1
    providers = []

    def __init__(self, scroller):
        self.scroller = scroller
        self._create_providers()

    def _create_providers(self):
        self.providers.append(DateProvider())
        self.providers.append(WeatherProvider("Madrid, ES"))
        self.providers.append(CryptoProvider(CoinId.ETHEREUM))
        self.providers.append(CryptoProvider(CoinId.BITCOIN))
        self.providers.append(TrendsProvider("23424950"))
        self.providers.append(RSSProvider("http://ep00.epimg.net/rss/tags/ultimas_noticias.xml"))
        for provider in self.providers:
            provider.initialize()

    def initialize(self):
        thread.start_new_thread(self._run, ())

    def _run(self):
        while True:
            provider = self._next_provider()
            text = provider.get_formatted_value()
            self.scroller.show_text(text)

    def _next_provider(self):
        next = self.providers[self._next_pointer()]
        while next.is_empty():
            next = self.providers[self._next_pointer()]
        return next

    def _next_pointer(self):
        value = self.pointer
        self.pointer = value + 1 if value + 1 < len(self.providers) else 0
        return self.pointer
