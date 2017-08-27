class TemperatureUnit(object):
    CELSIUS = "C"
    FAHRENHEIT = "F"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
