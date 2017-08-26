#!/usr/bin/env python


class CryptoCoin(object):
    def __init__(self, json):
        self.id = json["id"]
        self.name = json["name"]
        self.symbol = json["symbol"]
        self.price_usd = json["price_usd"]
        self.price_eur = json["price_eur"]
        self.percent_change_1h = json["percent_change_1h"]
        self.percent_change_24h = json["percent_change_24h"]
        self.percent_change_7d = json["percent_change_7d"]
        self.last_updated = json["last_updated"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
