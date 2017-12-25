# -*- coding: UTF-8 -*-
from presentation.formatter.formatter import Formatter


class Max7219CryptoFormatter(Formatter):
    _FORMAT = "{symbol} {price}\xee {percent_day}% 1D {percent_week}% 1W"

    def format(self, value):
        return self._FORMAT.format(
            symbol=self._format_symbol(value.symbol),
            price=self._format_price(value.price_eur),
            percent_day=self._format_percentage(value.percent_change_24h),
            percent_week=self._format_percentage(value.percent_change_7d))

    def _format_symbol(self, symbol):
        return symbol.lower().capitalize()

    def _format_price(self, price):
        return "%.2f" % float(price)

    def _format_percentage(self, percent):
        result = str(percent)
        if float(percent) > 0:
            result = "+" + result
        return result
