import unidecode

from formatter import Formatter


class AsciiFormatter(Formatter):
    def format(self, value):
        return unidecode.unidecode(value)


