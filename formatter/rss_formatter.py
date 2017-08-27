from formatter import Formatter


class RSSFormatter(Formatter):
    def format(self, value):
        return value[0].title
