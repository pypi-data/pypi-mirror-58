from typing import Optional, Union, List, Dict, Tuple
from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.ontology import Ontology, OntologyNode, DataRef, TrainingDataColumn
from datalogue.models.training import Training, ModelType, TrainingStatusType, OrderList, TrainingState, \
    training_status_type_from_str, Deployment, Section
from datalogue.errors import DtlError
from datalogue.utils import _parse_list, _parse_uuid
from uuid import UUID


class _DataClient:
    """
    Client to interact with TrainingData
    """
    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client

    def add(self, store_id: UUID, store_name: str, refs: List[DataRef], count: Optional[int] = None) -> Union[DtlError, List[UUID]]:
        """
        Attaches paths in the given `store_id` to the the nodes of the ontology.

        :param store_id: Id of the datastore that it going to be read
        :param store_name: Name of the datastore that it going to be read
        :param refs: List of data references to show which paths are going to be attached which ontology nodes
        :param count: Number of n first rows which we want to attach, if not passed we attach all rows
        :return: List of stream ids which are the jobs that is transferring data from datastore to Themis
        """
        stream_ids = []

        for dataRef in refs:
            for path in dataRef.path_list:

                # Creates a dataset per attachment as UI does.
                dataset_id = self.__create_dataset(store_name)
                if isinstance(dataset_id, DtlError):
                    return dataset_id
                
                stream_id = self.__transfer_data_from_datastore(store_id, dataset_id, dataRef.node_id, path, count)
                if isinstance(dataset_id, DtlError):
                    return stream_id

                self.__update_node(dataRef.node_id, path, dataset_id, stream_id)
                stream_ids.append(stream_id)
        return stream_ids

    def get_annotations(self, ontology_id: Union[str, UUID],
                        datastore_ids: List[Union[str, UUID]],
                        items_per_page: int = 25,
                        page_after_id: Union[str, UUID, None] = None) -> Union[DtlError, Tuple[List[Section], Optional[UUID]]]:
        """
        Retrieve a list of annotated sections tagged from an ontology, with full text, all associated annotations of that section, and other statistics.
        :param ontology_id: id of the ontology to retrieve annotated sections from
        :param datastore_ids: can be used to retrieve only sections imported from specified datastores, if None, will return all annotated sections
        :param items_per_page: the number of AnnotatedSections to return
        :param page_after_id: the id of an AnnotatedSection in sequence, after which the returned page begins
        :return: a list of AnnotatedSections with value which should be used as page_after_id in next call if successful,
         or DtlError if failed

        """
        # validate ontology_id
        ontology_id = _parse_uuid(ontology_id, f"The supplied ontology_id: {ontology_id} is not a valid UUID")
        if isinstance(ontology_id, DtlError):
            return ontology_id

        # validate page_after_id
        if page_after_id is not None:
            page_after_id = _parse_uuid(ontology_id, f"The supplied page_after_id: {page_after_id} is not a valid UUID")
            if isinstance(page_after_id, DtlError):
                return page_after_id
        after_query = f'&after={page_after_id}' if page_after_id is not None else ''
        uri = f"/themis/ontology/{ontology_id}/export-annotations-json?size={items_per_page}{after_query}"

        # validate datastore_ids
        datastore_ids = list(map(lambda datastore_id: _parse_uuid(datastore_id, f"The supplied datastoreId: {datastore_id} is not a valid UUID"), datastore_ids))
        for datastore_id in datastore_ids:
            if isinstance(datastore_id, DtlError):
                return datastore_id

        body = list(map(lambda datstore_id: str(datstore_id), datastore_ids))
        res = self.http_client.execute_authed_request(uri, HttpMethod.POST, body)

        if isinstance(res, DtlError):
            return res
        sections_statistics = _parse_list(Section.from_payload)(res.json())
        if isinstance(sections_statistics, DtlError):
            return sections_statistics
        next_token_raw = res.headers.get("X-Next-Token", None)
        next_token = _parse_uuid(next_token_raw) if next_token_raw is not None else None
        if isinstance(next_token, DtlError):
            return next_token
        return sections_statistics, next_token

    def __create_dataset(self, store_name: str) -> Union[DtlError, UUID]:
        payload = {
            "title": store_name,
            "tags": [],
            "label_map": {}
        }

        res = self.http_client.make_authed_request('/themis/dataset', HttpMethod.POST, body = payload)
        dataset_id = UUID(res.get("id"))

        if dataset_id is None:
            return DtlError("There is no dataset id in response!")
        return dataset_id

    def __transfer_data_from_datastore(self, store_id: UUID, dataset_id: UUID, node_id: UUID, path: List[str], count: Optional[int]) -> UUID:
        params = {
            'sourceId': str(store_id),
            'trainingDataId': str(dataset_id),
            'class': str(node_id),
            'path': path
        }
        if count is not None:
            params['count'] = count
        res = self.http_client.make_authed_request('/scout/run/training-data', HttpMethod.POST, params=params)
        stream_id = UUID(res["streamId"])
        return stream_id

    def __update_node(self, node_id: UUID, path: List[str], dataset_id: UUID, stream_id: UUID) -> List[str]:
        #TODO We should remove this part when we move training data adding functionality out of Yggy
        entity_res = self.http_client.make_authed_request(f"/yggy/entity/{node_id}", HttpMethod.GET)
        training_data_list = entity_res.get("trainingDataInfo")
        if training_data_list is None:
            training_data_list = []

        training_data_list.append({
            "datasetId": str(dataset_id),
            "nodePath": path,
            "streamId": str(stream_id)
        })

        self.http_client.make_authed_request(f"/yggy/entity/{node_id}", HttpMethod.POST,
            body={"trainingDataInfo": training_data_list})

        dataset_ids = []
        for trainingData in training_data_list:
            dataset_ids.append(trainingData["datasetId"])
        
        return dataset_ids

class _TrainingClient:
    """
    Client to interact with the Trainings
    """
    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.data = _DataClient(http_client)

    def list_deployed(self,
                      model_type: Optional[ModelType] = None,
                      page: int = 1,
                      item_per_page: int = 25) -> Union[DtlError, List[TrainingState]]:
        """
        Retrieve a list of all models currently deployed.

        :param model_type:
        :param page:
        :param item_per_page:
        :return:
        """
        from_item = (page-1)*item_per_page
        params = {
            'from': from_item,
            'limit': item_per_page,
            'status': 'Successful'
        }
        if model_type is not None:
            params['model-type'] = str(model_type)
        res = self.http_client.make_authed_request(
            f'/argus/deployments', HttpMethod.GET, params=params)
        if isinstance(res, DtlError):
            return res
        else:
            return _parse_list(Deployment._from_payload)(res)


    def deploy(self, training_id: UUID, ontology_id: UUID) -> Union[DtlError, bool]:
        """
        Deploy :class:`Training` based on the given training_id and ontology_id
        :return: True if successful, else returns :class:`DtlError`
        """
        res = self.http_client.make_authed_request(
            f'/yggy/ontology/{str(ontology_id)}/trainings/{str(training_id)}/deploy', 
            HttpMethod.POST, {})

        if isinstance(res, DtlError):
            return res
        else:
            return True

    #TODO API is not returning a training object, we should change this when the API returns training
    def run(self, ontology_id: UUID, model_type: ModelType) -> Union[DtlError, bool]:
        """
        Starts training for a given ontology_id

        :param ontology_id:
        :return: Either a :class:`DtlError` if any error occurs or :class:`True` if training is requested successfully.
        """
        params = dict()
        params["model-type"] = model_type.value

        res = self.http_client.make_authed_request(f"/yggy/ontology/{ontology_id}/train?model-type=cbc", HttpMethod.POST, params = params)

        if isinstance(res, DtlError):
            return res
        return True

    def get_trainings(self, ontology_id: UUID, model_type: Optional[ModelType] = None, status_type: Optional[TrainingStatusType] = None, sort: Optional[OrderList] = OrderList.desc, limit: Optional[int] = 20) -> Union[DtlError, List[TrainingState]]:
        """
        Get :class:`Trainings` based on the given ontology_id
        
        :param ontology_id:
        :return: List of trainings if successful, else returns :class:`DtlError`
        """

        params = {}

        if limit is not None:
            if not isinstance(limit, int) or limit < 0:
                return DtlError("limit should be a positive integer")
            params["limit"] = limit

        if model_type is not None:
            params["model-type"] = model_type.value
        
        if status_type is not None:
            params["status-type"] = status_type.value
        
        if sort is not None:
            params["sort"] = sort.value

        res = self.http_client.make_authed_request(f'/yggy/ontology/{str(ontology_id)}/trainings', HttpMethod.GET, params=params)

        if isinstance(res, DtlError):
            return res
        else:
            return _parse_list(TrainingState._from_payload)(res)

    def get(self, training_id: UUID)-> Union[DtlError, TrainingState]:
        """""
        Get :class:`Trainings` based on the given training_id

        :param training_id:
        :return: Requested training if successful, else returns :class:`DtlError`
        """

        res = self.http_client.make_authed_request(f'/argus/training/{str(training_id)}',
                                                    HttpMethod.GET)
        if isinstance(res, DtlError):
            return DtlError("Could not publish request.", res)

        return TrainingState._from_payload(res)

    def cancel(self, training_id: UUID) -> Union[DtlError, bool]:
        """
        Cancel training given a training_id

        :param training_id:
        :return: status of the training if successful, else returns :class:`DtlError`
        """

        res = self.http_client.make_authed_request(
            f'/argus/trainings/{str(training_id)}/cancel',
            HttpMethod.POST)

        if isinstance(res, DtlError):
            return res
        else:
            return True

    def get_model_url(self, training_id: UUID) -> Union[DtlError, Optional[str]]:
        """
        Return url of a deployment for a given training_id

        :param training_id:
        :return: url if there is an active deployment for the training, otherwise returns None
        """

        res = self.http_client.make_authed_request(f'/argus/deployments/model-url/{str(training_id)}', HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return res["url"]

    def get_training_history(self, ontology_id: UUID, limit: Optional[int] = 20) -> Union[DtlError, List[Training]]:
        """
        Get :class:`Training` history based on the given ontology_id
        
        :param ontology_id:
        :return: List of trainings if successful, else returns :class:`DtlError`
        """

        params = {}
        if limit is not None:
            if not isinstance(limit, int) or limit < 0:
                return DtlError("limit should be a positive integer")
            params["limit"] = limit
        
        res = self.http_client.make_authed_request(
            f'/yggy/ontology/{str(ontology_id)}/trainings/history',
            HttpMethod.GET, params=params)
        
        if isinstance(res, DtlError):
            return res
        else:
           return _parse_list(Training._from_payload)(res)
