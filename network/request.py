# -*- coding: UTF-8 -*-

import pycurl
import logging
from StringIO import StringIO


class Request(object):

    COOKIES_FILE = '/var/tmp/cookies.txt'
    VERBOSE = False
    TIMEOUT_IN_SECONDS = 30

    def __init__(self, url):
        self.url = url
        self.is_post = True
        self.headers = []
        self.data = ''
        self.pycurl = pycurl.Curl()
        self.buffer = StringIO()
        self.logger = logging.getLogger('request')

    def add_header(self, header):
        self.headers.append(header)

    def get_headers(self):
        return self.headers

    def set_headers(self, headers):
        self.headers = headers

    def add_cookie(self, cookie):
        self.pycurl.setopt(pycurl.COOKIE, cookie)

    def set_data(self, data):
        self.data = data

    def referer(self, referer):
        self.headers.append('Referer: ' + referer)

    def post(self):
        self._perform(True)

    def get(self):
        self._perform(False)

    def response(self):
        return self.buffer.getvalue()

    def close(self):
        self.buffer.close()

    def accept_gzip(self):
        self.pycurl.setopt(pycurl.ENCODING, 'gzip')

    def _perform(self, is_post):
        self.pycurl.setopt(pycurl.VERBOSE, self.VERBOSE)
        self.logger.info("Request: " + self.url)
        self.pycurl.setopt(pycurl.URL, self.url)
        self.pycurl.setopt(pycurl.SSL_VERIFYHOST, 0)
        self.pycurl.setopt(pycurl.SSL_VERIFYPEER, False)
        self.pycurl.setopt(pycurl.CONNECTTIMEOUT, self.TIMEOUT_IN_SECONDS)
        self.pycurl.setopt(pycurl.TIMEOUT, self.TIMEOUT_IN_SECONDS)
        self.pycurl.setopt(pycurl.WRITEFUNCTION, self.buffer.write)
        self.pycurl.setopt(pycurl.POST, is_post)
        self.pycurl.setopt(pycurl.COOKIEFILE, self.COOKIES_FILE)
        self.pycurl.setopt(pycurl.COOKIEJAR, self.COOKIES_FILE)
        self.pycurl.setopt(pycurl.FOLLOWLOCATION, False)
        if len(self.data) > 0:
            self.logger.debug("Body: " + self.data)
            self.pycurl.setopt(pycurl.POSTFIELDS, self.data)
            self.pycurl.setopt(pycurl.POSTFIELDSIZE, len(self.data))
        self.logger.debug("Headers: " + str(self.headers))
        self.pycurl.setopt(pycurl.HTTPHEADER, self.headers)
        self.pycurl.perform()
