import logging

import schedule

from domain.crypto.conversion import Conversion
from formatter.crypto_formatter import CryptoFormatter
from network.crypto_request import CryptoRequest
from provider import Provider


class CryptoProvider(Provider):

    _SCHEDULE_MINUTES = 15

    logger = logging.getLogger("data")

    def __init__(self, coin_id, conversion=Conversion.EUR):
        self.coin_id = coin_id
        self.conversion = conversion
        self.coin = None
        self.formatter = CryptoFormatter()

    def initialize(self):
        self._request_coin()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_coin)

    def get_value(self):
        return self.coin

    def get_formatted_value(self):
        return self.formatter.format(self.coin)

    def is_empty(self):
        return self.coin is None

    def _request_coin(self):
        request = CryptoRequest(self.coin_id, self.conversion)
        request.execute(self._on_result)

    def _on_result(self, coin):
        self.coin = coin
        self.logger.debug(coin)
