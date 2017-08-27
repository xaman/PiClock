import json
import urllib

from domain.temperature_unit import TemperatureUnit
from domain.weather import Weather
from network.request import Request


class WeatherRequest(Request):
    _ENDPOINT = "https://query.yahooapis.com/v1/public/yql?"
    _YQL = "select * from weather.forecast where woeid in (" \
           "select woeid from geo.places(1) where text='{location}'" \
           ") and u='{unit}'"
    _FORMAT = "&format=json"

    def __init__(self, location_name, temperature_unit=TemperatureUnit.CELSIUS):
        url = self._ENDPOINT + self._get_query(location_name, temperature_unit) + self._FORMAT
        super(WeatherRequest, self).__init__(url)

    def _get_query(self, location_name, temperature_unit):
        return urllib.urlencode({'q': self._YQL.format(
            location=location_name,
            unit=temperature_unit)})

    def execute(self, callback):
        self.get()
        json_response = json.loads(self.response())
        weather = Weather(json_response["query"]["results"]["channel"])
        callback(weather)
