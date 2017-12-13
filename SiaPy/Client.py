# -*- encoding: utf-8 -*-
#
# Copyright (c) 2017.
# All rights reserved.

import urllib, json

from requests import request, Session
from requests.packages import urllib3
from requests.exceptions import RequestException

from .Exceptions import HTTPError, SiadError

# Disable pyopenssl. It breaks SSL connection pool when SSL connection is
# closed unexpetedly by the server. And we don't need SNI anyway.
try:
    from requests.packages.urllib3.contrib import pyopenssl
    pyopenssl.extract_from_urllib3()
except ImportError:
    pass

# Disable SNI related Warning. The API does not rely on it
urllib3.disable_warnings(urllib3.exceptions.SNIMissingWarning)
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)


#: Default timeout for each request.
TIMEOUT = 5

class Client(object):
    """
    """

    def __init__(self, endpoint="127.0.0.1:9980", sia_agent="Sia-Agent", force_discover=False, auth_key=""):
        # Use Requests.Session to avoid any problem during the communication
        self._session = Session()

        self._endpoint = endpoint
        if not "http://" in self._endpoint:
            self._endpoint = "http://" + endpoint


        # Setup timeout
        self._timeout = TIMEOUT

        # Setup Custom Sia-agent
        self._sia_agent = sia_agent

        # Set API Auth Key
        self._auth_key = auth_key

        if(force_discover == True):
            self.daemon = self._discover_daemon()


    def _discover_daemon(self):
        req = self.get("/daemon/version")

        daemon = {"version": "0", "status": "disconnected"}
        if req.status_code == 200:
            datas = json.loads(req.text)
            daemon["version"] = datas['version']
            daemon["status"] = "connected"

        return daemon

    def get(self, _target):
        return self.call('GET', _target)

    def post(self, _target, params={}):
        return self.call('POST', _target, params)

    def call(self, _method, _target, params={}):

        body = ''
        target = self._endpoint + _target
        headers = {
            'User-Agent'    : self._sia_agent
        }

        if self._auth_key:
            headers['Authorization'] = "Basic %s" % self._auth_key

        try:
            resp = self._session.request(_method, target, headers=headers, data=body, timeout=self._timeout, params=params)
        except RequestException as error:
            raise HTTPError("Connection failed, Check your endpoint. (IP, DNS, Network...)", error)


        # Trigger Standar responses related to error (4xx, 5xx)
        if resp.status_code in {400, 401}:
            datas = json.loads(resp.text)
            raise SiadError(datas['message'])


        return resp










































