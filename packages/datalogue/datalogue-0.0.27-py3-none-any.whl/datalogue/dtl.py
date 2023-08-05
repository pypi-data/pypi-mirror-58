from datalogue.clients.http import _HttpClient
from datalogue.clients.jobs import _JobsClient
from datalogue.clients.datasets import _DatasetsClient
from datalogue.clients.workflow import _WorkflowClient
from datalogue.clients.credentials import _CredentialsClient
from datalogue.clients.datastore import _DataStoreClient
from datalogue.errors import DtlError

from validators import url


class DtlCredentials:
    """
    Information to be able to connect to the platform

    :param username: username to be used to login on the platform
    :param password: password to be used to login on the platform
    :param uri: root url where the system lives ie: https://test.datalogue.io/api
    """

    def __init__(self, username: str, password: str, uri: str):
        self.username = username
        self.password = password

        if url(uri) is not True:
            raise DtlError("The Uri you provided is not a valid")

        if not uri.endswith("/api"):
            raise DtlError("The Uri you provided doesn't end with '/api' it is most likely not valid")

        self.uri = uri

    def __repr__(self):
        return f'{self.__class__.__name__}(username: {self.username!r}, password: ****, uri: {self.uri!r})'


class Dtl:
    """
    Root class to be built to interact with all the services

    :param credentials: contains the information to connect
    """

    def __init__(self, credentials: DtlCredentials):
        self.uri = credentials.uri
        self.username = credentials.username
        self.http_client = _HttpClient(credentials.uri)

        login_res = self.http_client.login(credentials.username, credentials.password)
        if isinstance(login_res, str):
            raise DtlError(login_res)

        self.streams = _WorkflowClient(self.http_client)
        self.jobs = _JobsClient(self.http_client)
        self.datasets = _DatasetsClient(self.http_client)
        self.datastore = _DataStoreClient(self.http_client)
        self.credentials = _CredentialsClient(self.http_client)
        self.workflow = _WorkflowClient(self.http_client)

    def __repr__(self):
        return f'Logged in {self.uri!r} with {self.username!r} account)'
