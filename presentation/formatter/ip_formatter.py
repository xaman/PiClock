from presentation.formatter.formatter import Formatter


class IpFormatter(Formatter):
    _FORMAT = "{interface} addr {ip}"

    def format(self, value):
        return self._FORMAT.format(interface=value.name, ip=value.ip)
