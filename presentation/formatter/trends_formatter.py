from presentation.formatter.formatter import Formatter


class TrendsFormatter(Formatter):
    MAX_ITEMS = 5

    def __init__(self, ascii_formatter):
        super(TrendsFormatter, self).__init__()
        self.ascii_formatter = ascii_formatter

    def format(self, value):
        names = map(lambda trend: self.ascii_formatter.format(trend.name), value[:self.MAX_ITEMS])
        return ", ".join(names)
