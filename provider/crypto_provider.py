#!/usr/bin/env python
import json
import schedule

from model.crypto_coin import CryptoCoin
from model.crypto_conversion import CryptoConversion
from network.request import Request
from provider import Provider


class CryptoProvider(Provider):
    _SCHEDULE_MINUTES = 1
    _ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/{coin_id}/?convert={conversion}"

    def __init__(self, coin_id, conversion=CryptoConversion.EUR):
        self.coin_id = coin_id
        self.conversion = conversion
        self.coin = None

    def initialize(self):
        self._request_coin()
        schedule.every(self._SCHEDULE_MINUTES).minutes.do(self._request_coin)

    def get_value(self):
        return self.coin

    def is_empty(self):
        return self.coin is None

    def _request_coin(self):
        url = self._ENDPOINT.format(coin_id=self.coin_id.name, conversion=self.conversion.name)
        request = Request(url)
        request.get()
        json_response = json.loads(request.response())[0]
        self.coin = CryptoCoin(json_response)
        print self.coin
