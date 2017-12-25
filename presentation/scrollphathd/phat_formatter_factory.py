from presentation.formatter.ascii_formatter import AsciiFormatter
from presentation.formatter.crypto_formatter import CryptoFormatter
from presentation.formatter.date_formatter import DateFormatter
from presentation.formatter.formatter_factory import FormatterFactory
from presentation.formatter.ip_formatter import IpFormatter
from presentation.formatter.rss_formatter import RssFormatter
from presentation.formatter.trends_formatter import TrendsFormatter
from presentation.formatter.weather_formatter import WeatherFormatter


class PHatFormatterFactory (FormatterFactory):
    def get_crypto_formatter(self):
        return CryptoFormatter()

    def get_ascii_formatter(self):
        return AsciiFormatter()

    def get_rss_formatter(self):
        return RssFormatter()

    def get_trends_formatter(self):
        return TrendsFormatter()

    def get_date_formatter(self):
        return DateFormatter()

    def get_ip_formatter(self):
        return IpFormatter()

    def get_weather_formatter(self):
        return WeatherFormatter()
