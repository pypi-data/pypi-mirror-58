from typing import *
from enum import Enum
import requests
from datalogue.utils import Json
from datalogue.errors import DtlError


class HttpMethod(Enum):
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    DELETE = 'DELETE'


class _HttpClient:
    """
    Class that Abstracts aways requests and makes it use type safe.
    It also prepares all the requests to be used authenticated to the API
    """

    def __init__(self, uri: str):
        self.uri = uri
        self.http_session = requests.Session()

    def login(self, username: str, password: str) -> Union[DtlError, None]:
        """
        Sets the cookie for the client to use

        :return: Nothing
        """
        url = self.uri + '/signin'
        res = self.http_session.post(
            url,
            json={
                'email': username,
                'password': password
            },
            allow_redirects=False
        )

        if res.status_code != 201 and res.status_code != 302 and res.status_code != 200:
            return DtlError('Authentication failed - %s : %s' % (str(res.status_code), res.text))
        elif res.status_code == 503:
            return DtlError("The service is not available")
        else:
            return None

    def make_authed_request(self, path: str, method: HttpMethod, body: Optional[dict] = None) -> Union[DtlError, Json]:
        """
        Makes a request to the API give the url

        :param path: path to access the resource below the host
        :param method: parameter to indicate HTTP Method to be used in the request
        :param body: body to be sent along with the request
        :return: Request response
        """
        request_uri = self.uri + path
        req = requests.Request(method.value, request_uri, json=body)
        prepped = self.http_session.prepare_request(req)
        res = self.http_session.send(prepped)

        if res.status_code == 400:
            return DtlError("Invalid Request to %s returned 400, body res: %s" % (request_uri, res.text))

        if res.status_code == 401:
            return DtlError("Cookies have been invalidated by another session using the current credentials. "
                            "Please login again.")

        if res.status_code == 404:
            return DtlError("Route not found %s " % request_uri)

        if res.status_code == 500:
            return DtlError("Internal Server error")

        if res.status_code == 503:
            return DtlError("The service is not available")

        if method == HttpMethod.DELETE:
            return True
        else:
            content_type_header = res.headers.get("content-type")
            if len(res.text) > 0 and content_type_header == "application/json":
                return res.json()
            else:
                return res.text
