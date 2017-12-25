from ascii_formatter import AsciiFormatter
from presentation.formatter.formatter import Formatter


class TrendsFormatter(Formatter):
    MAX_ITEMS = 5

    ascii_formatter = AsciiFormatter()

    def format(self, value):
        names = map(lambda trend: self._format_ascii(trend.name), value[:self.MAX_ITEMS])
        return ", ".join(names)

    def _format_ascii(self, text):
        return self.ascii_formatter.format(text)
