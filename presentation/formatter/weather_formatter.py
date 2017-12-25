# -*- coding: UTF-8 -*-
from presentation.formatter.formatter import Formatter


class WeatherFormatter(Formatter):
    _FORMAT = "{city}, {temp}\xD4{unit} {text}"

    def format(self, value):
        return self._FORMAT.format(
            city=value.location.city,
            temp=value.condition.temp,
            unit=value.temperature_unit.value,
            text=value.condition.text.lower()
        )
