import random

from presentation.formatter.formatter import Formatter


class RssFormatter(Formatter):
    def __init__(self, ascii_formatter):
        super(RssFormatter, self).__init__()
        self.ascii_formatter = ascii_formatter

    def format(self, value):
        item = self._get_random(value)
        return self.ascii_formatter.format(item.title)

    def _get_random(self, items):
        return random.choice(items)
