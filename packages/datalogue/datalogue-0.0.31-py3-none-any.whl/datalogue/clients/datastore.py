from typing import List, Union
from uuid import UUID

from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.datastore import DataStore, _data_store_from_payload
from datalogue.errors import DtlError
from datalogue.utils import _parse_list


class _DataStoreClient:
    """
    Client to interact with the Resource objects
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.service_uri = "/scout"

    def create(self, resource: DataStore) -> Union[DtlError, DataStore]:
        """
        Creates a data source

        :param resource: data source to be created
        :return: string with error message if failed, the data source otherwise
        """
        res = self.http_client.make_authed_request(
            self.service_uri + "/source", HttpMethod.POST, resource._as_payload())

        if isinstance(res, DtlError):
            return res

        return _data_store_from_payload(res)

    def update(self, resource: DataStore) -> Union[DtlError, DataStore]:
        """
        Updates the backend with the new status of the existing resource

        :param resource: to be persisted
        :return:
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/source/" + str(resource.id),
            HttpMethod.POST,
            resource._as_payload()
        )

        if isinstance(res, DtlError):
            return res

        return _data_store_from_payload(res)

    def list(self, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[DataStore]]:
        """
        List all the data stores that are saved

        TODO pagination

        :param page: page to be retrieved (ignored)
        :param item_per_page: number of items to be put in a page (ignored)
        :return: Returns a List of all the available data stores or an error message as a string
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/sources", HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _parse_list(_data_store_from_payload)(res)

    def get(self, resource_id: UUID) -> Union[DtlError, DataStore]:
        """
        From the provided id, get the corresponding Datastore

        :param resource_id: id of the data store to be retrieved
        :return:
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/source/" + str(resource_id), HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _data_store_from_payload(res)

    def delete(self, resource_id: UUID) -> Union[DtlError, bool]:
        """
        Deletes the given Resource

        :param resource_id: id of the resource to be deleted
        :return: true if successful, false otherwise
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/source/" + str(resource_id), HttpMethod.DELETE)

        if isinstance(res, DtlError):
            return res
        else:
            return True
