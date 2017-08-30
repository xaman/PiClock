import schedule

from network.weather_request import WeatherRequest
from provider import Provider


class WeatherProvider(Provider):
    _SCHEDULE_MINUTES = 15

    def __init__(self, location_name, formatter):
        super(WeatherProvider, self).__init__()
        self.location_name = location_name
        self.formatter = formatter

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        request = WeatherRequest(self.location_name)
        request.execute(self._on_result)

    def _on_result(self, data):
        self.data = data
        self.logger.debug(data)
