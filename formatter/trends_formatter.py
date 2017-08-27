from formatter import Formatter


class TrendsFormatter(Formatter):
    def format(self, value):
        return ", ".join(map(lambda trend: trend.name, value[:10]))
