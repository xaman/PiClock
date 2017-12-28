from presentation.max7219.formatter.max7219_ascii_formatter import Max7219AsciiFormatter
from presentation.max7219.formatter.max7219_crypto_formatter import Max7219CryptoFormatter
from presentation.max7219.formatter.max7219_weather_formatter import Max7219WeatherFormatter

from presentation.formatter.ascii_formatter import AsciiFormatter
from presentation.formatter.rss_formatter import RssFormatter
from presentation.formatter.date_formatter import DateFormatter
from presentation.formatter.formatter_factory import FormatterFactory
from presentation.formatter.ip_formatter import IpFormatter
from presentation.formatter.trends_formatter import TrendsFormatter


class Max7219FormatterFactory(FormatterFactory):
    def get_crypto_formatter(self):
        return Max7219CryptoFormatter()

    def get_ascii_formatter(self):
        return AsciiFormatter()

    def get_rss_formatter(self):
        return RssFormatter(Max7219AsciiFormatter())

    def get_trends_formatter(self):
        return TrendsFormatter(Max7219AsciiFormatter())

    def get_date_formatter(self):
        return DateFormatter()

    def get_ip_formatter(self):
        return IpFormatter()

    def get_weather_formatter(self):
        return Max7219WeatherFormatter()
