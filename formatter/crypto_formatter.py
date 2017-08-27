from formatter import Formatter


class CryptoFormatter(Formatter):
    def format(self, value):
        return "{symbol} {price}EUR {percent}%".format(
            symbol=value.symbol,
            price=self._format_price(value.price_eur),
            percent=self._format_percentage(value.percent_change_24h))

    def _format_price(self, price):
        return "%.2f" % float(price)

    def _format_percentage(self, percent):
        result = str(percent)
        if float(percent) > 0:
            result = "+" + result
        return result
