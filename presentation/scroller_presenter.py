import logging

import thread

from domain.crypto.coin_id import CoinId
from formatter.crypto_formatter import CryptoFormatter
from formatter.rss_formatter import RSSFormatter
from formatter.trends_formatter import TrendsFormatter
from formatter.weather_formatter import WeatherFormatter
from provider.crypto_provider import CryptoProvider
from provider.date_provider import DateProvider
from provider.rss_provider import RSSProvider
from provider.trends_provider import TrendsProvider
from provider.weather_provider import WeatherProvider


class ScrollerPresenter(object):
    logger = logging.getLogger()
    pointer = -1
    providers = []
    show_clock = True

    def __init__(self, scroller):
        self.scroller = scroller
        self._create_providers()

    def _create_providers(self):
        self.providers.append(DateProvider())
        self.providers.append(WeatherProvider("Madrid, ES", WeatherFormatter()))
        self.providers.append(CryptoProvider(CoinId.ETHEREUM, CryptoFormatter()))
        self.providers.append(CryptoProvider(CoinId.BITCOIN, CryptoFormatter()))
        self.providers.append(TrendsProvider("23424950", TrendsFormatter()))
        # self.providers.append(RSSProvider("http://ep00.epimg.net/rss/tags/ultimas_noticias.xml", RSSFormatter()))
        for provider in self.providers:
            provider.initialize()

    def initialize(self):
        thread.start_new_thread(self._run, ())

    def _run(self):
        while True:
            if self.show_clock:
                self._show_clock()
            else:
                self._show_provider()
            self.show_clock = not self.show_clock

    def _show_clock(self):
        self.scroller.show_clock()

    def _show_provider(self):
        provider = self.providers[self._next_pointer()]
        if not provider.is_empty():
            text = provider.get_formatted_value()
            self.scroller.show_text(text)

    def _next_pointer(self):
        value = self.pointer
        self.pointer = value + 1 if value + 1 < len(self.providers) else 0
        return self.pointer
