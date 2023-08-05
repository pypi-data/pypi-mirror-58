from typing import List, Union, Optional
from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.stream import Stream
from datalogue.models.workflow import Workflow, _workflow_from_payload, _stream_metadata_from_payload
from datalogue.utils import _parse_list
from datalogue.errors import DtlError
from uuid import UUID, uuid4
from datetime import datetime
from dateutil.tz import UTC


class _WorkflowClient:
    """
    Right now interactions on workflows as they are currently called in the API. Or Pipeline as they are
    called in the UI.

    To simplify things, right now the SDK allows interactions with workflow of one stream
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.service_uri = "/scout"

    def create(self, streams: List[Stream], name: Optional[str]) -> Union[DtlError, Workflow]:
        """
        Creates the stream as specified.
        Right now this creates a Workflow with only one stream

        TODO think about creating datastores when they are references in the Stream that don't exist

        :param streams: Streams to be created
        :param name: name of the stream to be created. If None supplied, one will be generated
        :return: string with error message if failed, uuid otherwise
        """

        if name is None:
            name = "stream-" + str(uuid4())[0:8]

        # save workflow
        res1 = self.http_client.make_authed_request(
            self.service_uri + '/workflow', HttpMethod.POST, {"name": name}
        )

        workflow_id = res1.get("id")
        if workflow_id is None:
            return DtlError("Created response did not return an id")

        created_streams = []
        # add stream
        for stream in streams:
            res2 = self.http_client.make_authed_request(
                self.service_uri + '/workflow/' + workflow_id + "/stream", HttpMethod.POST, stream._as_payload()
            )
            if isinstance(res2, DtlError):
                return res2

            stream_meta = _stream_metadata_from_payload(res2)
            if isinstance(stream_meta, DtlError):
                return stream_meta

            created_streams.append(stream_meta)

        return Workflow(workflow_id, name, created_streams)

    def update(self, workflow_id: UUID, name: Optional[str] = None, streams: Optional[List[Stream]] = None) \
            -> Union[DtlError, Workflow]:
        """
        Updates the workflow

        :param workflow_id: id of the workflow to update
        :param name: new name of the workflow
        :param streams: new set of streams for the workflow (overrides the previous set)
        :return: Either an error message in a string or the workflow
        """

        ref_workflow = self.get(workflow_id)
        if isinstance(ref_workflow, DtlError):
            return DtlError("It looks like you are trying to update a workflow that doesn't exist", ref_workflow)

        if isinstance(name, str):

            res = self.http_client.make_authed_request(
                f"{self.service_uri}/workflow/{workflow_id}", HttpMethod.POST, {"name": name}
            )

            if isinstance(res, DtlError):
                return res

        if isinstance(streams, list):

            # We start by removing all the existing streams
            for stream in ref_workflow.streams:
                res = self.http_client.make_authed_request(f"{self.service_uri}/stream/{stream.id}", HttpMethod.DELETE)
                if isinstance(res, DtlError):
                    return DtlError("Could not delete all previously existing streams, interrupting update", res)

            # Then we attach all the new ones
            for stream in streams:
                res = self.http_client.make_authed_request(
                    f"{self.service_uri}/workflow/{workflow_id}/stream", HttpMethod.POST, stream._as_payload()
                )
                if isinstance(res, DtlError):
                    return DtlError("Could not add all the new streams to the workflow, interrupting update", res)

        return self.get(workflow_id)

    def schedule(self, workflow_id: UUID, date: datetime) -> Union[DtlError, bool]:
        """
        Creates a job to be run at the given date

        :param workflow_id: id of the stream to be run
        :param date: date at which to run the stream, expected to be localized
        :return: Either an error message in a string or the UUID for the new job
        """

        res = self.http_client.make_authed_request(
            self.service_uri + '/workflow/' + str(workflow_id) + "/schedule",
            HttpMethod.POST,
            {"runDate": date.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}
        )

        if isinstance(res, DtlError):
            return res

        return True

    def list(self, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[Workflow]]:
        """
        Retrieves a list of the available streams (workflow)

        TODO pagination
        :param page: page to be retrieved
        :param item_per_page: number of items to be put in a page
        :return: Returns a List of all the available streams or an error message as a string
        """
        res = self.http_client.make_authed_request(self.service_uri + "/workflows", HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _parse_list(_workflow_from_payload)(res)

    def get(self, workflow_id: UUID) -> Union[DtlError, Workflow]:
        """
        From the provided id, get the corresponding stream (workflow)

        :param workflow_id:
        :return:
        """
        res = self.http_client.make_authed_request(
            self.service_uri + "/workflow/" + str(workflow_id), HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _workflow_from_payload(res)

    def delete(self, workflow_id: UUID) -> Union[DtlError, bool]:
        """
        Deletes the given stream (workflow)

        :param workflow_id: id of the stream (workflow) to be deleted
        :return: true if successful, false otherwise
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/workflow/" + str(workflow_id), HttpMethod.DELETE)

        if isinstance(res, DtlError):
            return res
        else:
            return True
