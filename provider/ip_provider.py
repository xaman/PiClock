import socket
import fcntl
import struct

from provider import Provider


class IPProvider(Provider):
    _FORMAT = "{interface} addr {ip}"

    def __init__(self, interface):
        super(IPProvider, self).__init__()
        self.interface = interface

    def initialize(self):
        pass

    def is_empty(self):
        return False

    def get_value(self):
        self.data = self._get_ip_address(self.interface)
        return self._FORMAT.format(interface=self.interface, ip=self.data)

    def get_formatted_value(self):
        return self.get_value()

    def _get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
