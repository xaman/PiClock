class Trend(object):
    def __init__(self, json):
        self.name = json["name"]
        self.url = json["url"]
        self.tweet_volume = json["tweet_volume"]

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
