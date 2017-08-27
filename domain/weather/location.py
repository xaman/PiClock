class Location(object):
    def __init__(self, json):
        self.city = json["city"]
        self.region = json["region"]
        self.country = json["country"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
