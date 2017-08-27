from formatter import Formatter
from ascii_formatter import AsciiFormatter


class RSSFormatter(Formatter):
    ascii_formatter = AsciiFormatter()

    def format(self, value):
        return self._format_ascii(value[0].title)

    def _format_ascii(self, text):
        return self.ascii_formatter.format(text)
