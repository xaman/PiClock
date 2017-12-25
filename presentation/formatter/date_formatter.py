from presentation.formatter.formatter import Formatter


class DateFormatter(Formatter):
    _FORMAT = "%a, %-d %b '%y"

    def format(self, value):
        return value.strftime(self._FORMAT)
