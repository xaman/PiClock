# -*- coding: UTF-8 -*-


from formatter import Formatter


class WeatherFormatter(Formatter):
    def format(self, value):
        return "{temp}{unit}º {text} in {city}, {country}".format(
            temp=value.condition.temp,
            unit=value.temperature_unit.value,
            text=value.condition.text,
            city=value.location.city,
            country=value.location.country
        )
