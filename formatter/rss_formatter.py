import random

from formatter import Formatter
from ascii_formatter import AsciiFormatter


class RSSFormatter(Formatter):
    ascii_formatter = AsciiFormatter()

    def format(self, value):
        item = self._get_random(value)
        return self._format_ascii(item.title)

    def _get_random(self, items):
        return random.choice(items)

    def _format_ascii(self, text):
        return self.ascii_formatter.format(text)
