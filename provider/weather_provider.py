import logging

import schedule

from formatter.weather_formatter import WeatherFormatter
from network.weather_request import WeatherRequest
from provider import Provider


class WeatherProvider(Provider):

    _SCHEDULE_MINUTES = 30

    logger = logging.getLogger("data")

    def __init__(self, location_name):
        self.location_name = location_name
        self.weather = None
        self.formatter = WeatherFormatter()

    def initialize(self):
        self._request_weather()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_weather)

    def get_value(self):
        return self.weather

    def get_formatted_value(self):
        return self.formatter.format(self.weather)

    def is_empty(self):
        return self.weather is None

    def _request_weather(self):
        request = WeatherRequest(self.location_name)
        request.execute(self._on_result)

    def _on_result(self, weather):
        self.weather = weather
        self.logger.debug(weather)
