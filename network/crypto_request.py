import json

from domain.crypto.coin import Coin
from network.request import Request


class CryptoRequest(Request):
    _ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/{coin_id}/?convert={conversion}"

    def __init__(self, coin_id, conversion):
        url = self._ENDPOINT.format(coin_id=coin_id.name, conversion=conversion.name)
        super(CryptoRequest, self).__init__(url)

    def execute(self, callback):
        self.get()
        json_response = json.loads(self.response())[0]
        coin = Coin(json_response)
        callback(coin)
