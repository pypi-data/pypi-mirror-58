from typing import List, Union, Optional
from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.datastore import DataStore
from datalogue.models.access import Access, _access_ref_from_payload, AccessReference
from datalogue.utils import _parse_list
from uuid import UUID
from datalogue.errors import DtlError


class _CredentialsClient:
    """
    Client to interact with the Credentials objects
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.service_uri = "/scout"

    def create(self, access_definition: Access, name: Optional[str] = None) -> Union[DtlError, AccessReference]:
        """
        Creates the Resource as specified.

        :param access_definition: Access Definition to be creates
        :param name: Name to be given to the credentials to be able to find it later
        :return: string with error message if failed, uuid otherwise
        """
        res = self.http_client.make_authed_request(self.service_uri + "/credentials", HttpMethod.POST, {
            "name": name,
            "credentials": access_definition._as_payload()
        })

        if isinstance(res, DtlError):
            return res

        return _access_ref_from_payload(res)

    def update(self, credentials_id: UUID, access_definition: Access,
               name: Optional[str] = None) -> Union[DtlError, AccessReference]:
        """
        Updates the given credentials id with name and credentials

        TODO rework the api so that you can only update the name without the credentials themselves

        :param credentials_id: id of te credentials to update
        :param name: if specified, will overwrite current name
        :param access_definition: new credentials definition
        :return:
        """

        body = {}
        if name is not None:
            body["name"] = name

        body["credentials"] = access_definition._as_payload()

        res = self.http_client.make_authed_request(
            self.service_uri + "/credentials/" + str(credentials_id),
            HttpMethod.PUT,
            body
        )

        if isinstance(res, DtlError):
            return res

        return _access_ref_from_payload(res)

    def list(self, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[DataStore]]:
        """
        Lists available credentials

        TODO Pagination!

        :param page: page to be retrieved (ignored for now)
        :param item_per_page: number of items to be put in a page (ignored for now)
        :return: Returns a List of all the available credentials or an error message as a string
        """

        res = self.http_client.make_authed_request(self.service_uri + "/credentials", HttpMethod.GET)

        if isinstance(res, str):
            return res

        return _parse_list(_access_ref_from_payload)(res)

    def delete(self, credentials_id: UUID) -> Union[DtlError, bool]:
        """
        Deletes the given credentials

        :param credentials_id: id of the resource to be deleted
        :return: true if successful, false otherwise
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/credentials/" + str(credentials_id),
            HttpMethod.DELETE
        )

        if isinstance(res, DtlError):
            return res
        else:
            return True
