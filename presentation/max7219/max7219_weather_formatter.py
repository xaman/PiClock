# -*- coding: UTF-8 -*-
from presentation.formatter.weather_formatter import WeatherFormatter


class Max7219WeatherFormatter(WeatherFormatter):
    _FORMAT = "{city}, {temp}\xf8{unit} {text}"

    def format(self, value):
        return super(Max7219WeatherFormatter, self).format(value)
