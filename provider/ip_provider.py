import socket
import fcntl
import struct

from domain.network_interface import NetworkInterface
from provider import Provider


class IpProvider(Provider):
    def __init__(self, interface, formatter):
        super(IpProvider, self).__init__()
        self.interface = interface
        self.formatter = formatter

    def initialize(self):
        pass

    def is_empty(self):
        return False

    def get_data(self):
        ip = self._get_ip_address(self.interface)
        self.data = NetworkInterface(self.interface, ip)
        return self.formatter.format(self.data)

    def _get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
