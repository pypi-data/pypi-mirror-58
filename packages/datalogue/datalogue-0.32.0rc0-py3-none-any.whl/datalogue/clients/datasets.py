from typing import List, Union
from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.dataset import Dataset, _dataset_from_dict
from datalogue.errors import DtlError
from uuid import UUID
from datalogue.utils import _parse_list


class _DatasetsClient:
    """
    Client to interact with the datasets objects
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.service_uri = "/scout"

    def create(self, dataset: Dataset) -> Union[DtlError, Dataset]:
        """
        Creates the Dataset as specified.

        :param dataset: Dataset to be created
        :return: string with error message if failed, uuid otherwise
        """
        assert isinstance(dataset, Dataset), 'Input is not a Dataset instance.'
        # todo?? assert datastore indeed is a datastore

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets", HttpMethod.POST,
            dataset._as_payload())

        if isinstance(res, DtlError):
            return res

        return _dataset_from_dict(res)

    def update(self, dataset_id: UUID, dataset: Dataset) -> Union[DtlError, bool]:
        """
        Updates the Dataset for the given dataset_id

        :param dataset_id: Id of the dataset to update
        :param dataset: Dataset to be updated
        :return: string with error message if failed, uuid otherwise
        """
        assert isinstance(dataset, Dataset), 'Input is not a Dataset instance.'

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets/" + str(dataset_id), HttpMethod.PUT,
            dataset._as_payload())


        if isinstance(res, DtlError):
            return res
        else:
            return True

    def search(self, query: str, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[Dataset]]:
        """
        Search through the datasets

        :param query: text query to be used to make the search
        :param page: page to be retrieved
        :param item_per_page: number of items to be put in a page
        :return: Returns a List of all the available streams or an error message as a string
        """

        assert isinstance(query, str), 'Input query must be a string.'

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets?", HttpMethod.GET, )

        if isinstance(res, DtlError):
            return res

        out_list = []

        for i in range(len(res)):
            for content in res[i].values():
                if query in str(content):
                    out_list.append(res[i])
                    break

        # Todo build pagination
        return _parse_list(_dataset_from_dict)(out_list)

    def list(self, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[Dataset]]:
        """
        List the datasets

        :param page: page to be retrieved
        :param item_per_page: number of items to be put in a page
        :return: Returns a List of all the available datasets or an error message as a string
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets?", HttpMethod.GET, )

        if isinstance(res, DtlError):
            return res

        # Todo build pagination
        return _parse_list(_dataset_from_dict)(res)

    def get(self, dataset_id: UUID) -> Union[DtlError, Dataset]:
        """
        From the provided id, get the corresponding dataset

        :param dataset_id:
        :return:
        """
        assert isinstance(dataset_id, UUID), 'Input is not a UUID instance.'

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets/" + str(dataset_id),
            HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _dataset_from_dict(res)

    def delete(self, dataset_id: UUID) -> Union[DtlError, bool]:
        """
        Deletes the given dataset

        :param dataset_id: id of the dataset to be deleted
        :return: true if successful, the error otherwise
        """
        assert isinstance(dataset_id, UUID), 'Input is not a UUID instance.'

        res = self.http_client.make_authed_request(
            self.service_uri + "/datasets/" + str(dataset_id),
            HttpMethod.DELETE
        )

        if isinstance(res, DtlError):
            return res
        else:
            return True
