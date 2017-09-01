from bs4 import BeautifulSoup

from data.network.request import Request
from domain.rss_item import RSSItem


class RssRequest(Request):
    def __init__(self, url):
        super(RssRequest, self).__init__(url)

    def execute(self, callback):
        response = self.get().response()
        if response:
            html = BeautifulSoup(response, 'html.parser')
            items = map(lambda tag: RSSItem(tag), html.find_all("item"))
            callback(items)
        else:
            callback(None)
