from datetime import date

from provider import Provider


class DateProvider(Provider):
    FORMAT = "%A, %d %B %Y"

    def initialize(self):
        pass

    def get_value(self):
        return date.today().strftime(self.FORMAT)

    def get_formatted_value(self):
        return self.get_value()
