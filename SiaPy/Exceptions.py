# -*- encoding: utf-8 -*-

class APIError(Exception):
    """An API Error Exception"""
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)

        # TODO Manage response

    def __str__(self):
    	return super(APIError, self).__str__()

class HTTPError(APIError):
    """Raised when the request fails during the connection (IP, DNS, Network...)"""

class GatewayError(APIError):
    """Raised by the endpoint /gateway"""

class SiadError(APIError):
	"""Raised when the API return a 40x code error"""
