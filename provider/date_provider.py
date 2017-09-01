from datetime import date

from provider import Provider


class DateProvider(Provider):
    def __init__(self, formatter):
        super(DateProvider, self).__init__()
        self.formatter = formatter

    def initialize(self):
        pass

    def is_empty(self):
        return False

    def get_value(self):
        return self.formatter.format(date.today())

    def get_formatted_value(self):
        return self.get_value()
