# -*- coding: UTF-8 -*-
from formatter import Formatter


class CryptoFormatter(Formatter):
    _FORMAT = "{symbol} {price}\xC0 {percent}%"

    def format(self, value):
        return self._FORMAT.format(
            symbol=self._format_symbol(value.symbol),
            price=self._format_price(value.price_eur),
            percent=self._format_percentage(value.percent_change_24h))

    def _format_symbol(self, symbol):
        return symbol.lower().capitalize()

    def _format_price(self, price):
        return "%.2f" % float(price)

    def _format_percentage(self, percent):
        result = str(percent)
        if float(percent) > 0:
            result = "+" + result
        return result
