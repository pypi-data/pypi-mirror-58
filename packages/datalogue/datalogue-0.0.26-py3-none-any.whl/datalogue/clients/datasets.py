from typing import List, Union
from datalogue.clients.http import _HttpClient
from datalogue.models.dataset import Dataset
from datalogue.errors import DtlError
from uuid import UUID


class _DatasetsClient:
    """
    Client to interact with the datasets objects
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client

    def create(self, dataset: Dataset) -> Union[DtlError, UUID]:
        """
        Creates the Dataset as specified.

        :param dataset: Dataset to be created
        :return: string with error message if failed, uuid otherwise
        """

    def search(self, query: str, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[Dataset]]:
        """
        Search through the datasets

        :param query: text query to be used to make the search
        :param page: page to be retrieved
        :param item_per_page: number of items to be put in a page
        :return: Returns a List of all the available streams or an error message as a string
        """

    def get(self, dataset_id: UUID) -> Union[DtlError, Dataset]:
        """
        From the provided id, get the corresponding dataset

        :param dataset_id:
        :return:
        """

    def delete(self, dataset_id: UUID) -> bool:
        """
        Deletes the given dataset

        :param dataset_id: id of the dataset to be deleted
        :return: true if successful, false otherwise
        """