from formatter import Formatter


class TrendsFormatter(Formatter):
    MAX_ITEMS = 10

    def format(self, value):
        return ", ".join(map(lambda trend: trend.name, value[:self.MAX_ITEMS]))
