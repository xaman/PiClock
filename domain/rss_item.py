class RSSItem(object):
    def __init__(self, html):
        self.title = html.title.string
        self.link = html.link.string
        self.description = html.description.string

    def __str__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join('%s=%s' % item for item in vars(self).items()))
