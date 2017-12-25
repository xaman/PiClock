from presentation.formatter.empty_formatter import EmptyFormatter


class FormatterFactory(object):
    def get_ascii_formatter(self):
        return EmptyFormatter()

    def get_crypto_formatter(self):
        return EmptyFormatter()

    def get_date_formatter(self):
        return EmptyFormatter()

    def get_ip_formatter(self):
        return EmptyFormatter()

    def get_rss_formatter(self):
        return EmptyFormatter()

    def get_trends_formatter(self):
        return EmptyFormatter()

    def get_weather_formatter(self):
        return EmptyFormatter()
