from datetime import date

from provider import Provider


class DateProvider(Provider):
    FORMAT = "%a, %d %b '%y"

    def initialize(self):
        pass

    def is_empty(self):
        return False

    def get_value(self):
        return date.today().strftime(self.FORMAT)

    def get_formatted_value(self):
        return self.get_value()
