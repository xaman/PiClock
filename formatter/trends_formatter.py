from formatter import Formatter
from ascii_formatter import AsciiFormatter


class TrendsFormatter(Formatter):
    MAX_ITEMS = 5

    ascii_formatter = AsciiFormatter()

    def format(self, value):
        names = map(lambda trend: self._format_ascii(trend.name), value)
        return ", ".join(names[:self.MAX_ITEMS])

    def _format_ascii(self, text):
        return self.ascii_formatter.format(text)
