# -*- coding: UTF-8 -*-


from formatter import Formatter


class WeatherFormatter(Formatter):
    def format(self, value):
        return "{city}, {temp}{unit} {text}".format(
            city=value.location.city,
            temp=value.condition.temp,
            unit=value.temperature_unit.value,
            text=value.condition.text
        )
