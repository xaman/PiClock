class NetworkInterface(object):
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
