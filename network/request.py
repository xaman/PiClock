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
        self.curl = pycurl.Curl()
        self.buffer = StringIO()
        self.logger = logging.getLogger('data')

    def add_header(self, header):
        self.headers.append(header)
        return self

    def get_headers(self):
        return self.headers

    def set_headers(self, headers):
        self.headers = headers
        return self

    def add_cookie(self, cookie):
        self.curl.setopt(pycurl.COOKIE, cookie)
        return self

    def set_data(self, data):
        self.data = data
        return self

    def referer(self, referer):
        self.headers.append('Referer: ' + referer)
        return self

    def post(self):
        self._perform(True)
        return self

    def get(self):
        self._perform(False)
        return self

    def response(self):
        return self.buffer.getvalue()

    def close(self):
        self.buffer.close()

    def accept_gzip(self):
        self.curl.setopt(pycurl.ENCODING, 'gzip')

    def _perform(self, is_post):
        self.curl.setopt(pycurl.VERBOSE, self.VERBOSE)
        self.logger.debug("Request: " + self.url)
        self.curl.setopt(pycurl.URL, self.url)
        self.curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        self.curl.setopt(pycurl.SSL_VERIFYPEER, False)
        self.curl.setopt(pycurl.CONNECTTIMEOUT, self.TIMEOUT_IN_SECONDS)
        self.curl.setopt(pycurl.TIMEOUT, self.TIMEOUT_IN_SECONDS)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buffer.write)
        self.curl.setopt(pycurl.POST, is_post)
        self.curl.setopt(pycurl.COOKIEFILE, self.COOKIES_FILE)
        self.curl.setopt(pycurl.COOKIEJAR, self.COOKIES_FILE)
        self.curl.setopt(pycurl.FOLLOWLOCATION, False)
        if len(self.data) > 0:
            self.logger.debug("Body: " + self.data)
            self.curl.setopt(pycurl.POSTFIELDS, self.data)
            self.curl.setopt(pycurl.POSTFIELDSIZE, len(self.data))
        self.logger.debug("Headers: " + str(self.headers))
        self.curl.setopt(pycurl.HTTPHEADER, self.headers)
        try:
            self.curl.perform()
        except pycurl.error, e:
            self.logger.error(str(e))
