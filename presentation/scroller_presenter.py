import logging
import thread

from data.provider.crypto_provider import CryptoProvider
from data.provider.ip_provider import IpProvider
from data.provider.rss_provider import RssProvider
from data.provider.trends_provider import TrendsProvider
from data.provider.weather_provider import WeatherProvider

from data.provider.date_provider import DateProvider
from domain.crypto.coin_id import CoinId
from presentation.formatter.crypto_formatter import CryptoFormatter
from presentation.formatter.date_formatter import DateFormatter
from presentation.formatter.ip_formatter import IpFormatter
from presentation.formatter.rss_formatter import RssFormatter
from presentation.formatter.trends_formatter import TrendsFormatter
from presentation.formatter.weather_formatter import WeatherFormatter


class ScrollerPresenter(object):
    logger = logging.getLogger()
    pointer = -1
    providers = []
    show_clock = True

    def __init__(self, scroller):
        self.scroller = scroller
        self._create_providers()

    def _create_providers(self):
        self.providers.append(DateProvider(DateFormatter()))
        self.providers.append(WeatherProvider(location_name="Madrid, ES", formatter=WeatherFormatter()))
        self.providers.append(WeatherProvider(location_name="London, England", formatter=WeatherFormatter()))
        self.providers.append(CryptoProvider(coin_id=CoinId.ETHEREUM, formatter=CryptoFormatter()))
        self.providers.append(CryptoProvider(coin_id=CoinId.BITCOIN, formatter=CryptoFormatter()))
        self.providers.append(TrendsProvider(woeid="23424950", formatter=TrendsFormatter()))
        self.providers.append(RssProvider(url="http://ep00.epimg.net/rss/tags/ultimas_noticias.xml", formatter=RssFormatter()))
        self.providers.append(IpProvider(interface="wlan0", formatter=IpFormatter()))

    def initialize(self):
        thread.start_new_thread(self._initialize_providers, ())
        thread.start_new_thread(self._run, ())

    def _initialize_providers(self):
        for provider in self.providers:
            provider.initialize()

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
            text = provider.get_data()
            self.scroller.show_text(text)

    def _next_pointer(self):
        value = self.pointer
        self.pointer = value + 1 if value + 1 < len(self.providers) else 0
        return self.pointer
