import schedule

from network.rss_request import RSSRequest
from provider import Provider


class RSSProvider(Provider):
    _SCHEDULE_MINUTES = 10

    def __init__(self, url, formatter):
        super(RSSProvider, self).__init__()
        self.url = url
        self.formatter = formatter

    def initialize(self):
        self._request_data()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_data)

    def _request_data(self):
        RSSRequest(self.url).execute(self._on_result)

    def _on_result(self, items):
        self.data = items
