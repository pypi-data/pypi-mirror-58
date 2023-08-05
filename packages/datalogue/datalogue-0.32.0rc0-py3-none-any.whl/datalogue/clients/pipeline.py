from typing import List, Union, Optional
from datalogue.clients.http import _HttpClient, HttpMethod
from datalogue.models.stream import Stream
from datalogue.models.pipeline import Pipeline, _pipeline_from_payload, _stream_metadata_from_payload
from datalogue.utils import _parse_list
from datalogue.errors import DtlError
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from dateutil.tz import UTC


class _PipelineClient:
    """
    Right now interactions on pipelines as they are currently called in the API. Or Pipeline as they are
    called in the UI.

    To simplify things, right now the SDK allows interactions with pipeline of one stream
    """

    def __init__(self, http_client: _HttpClient):
        self.http_client = http_client
        self.service_uri = "/scout"

    def create(self, streams: List[Stream], name: Optional[str]) -> Union[DtlError, Pipeline]:
        """
        Creates the stream as specified.
        Right now this creates a pipeline with only one stream

        TODO think about creating resources when they are references in the Stream that don't exist

        :param streams: Streams to be created
        :param name: name of the stream to be created. If None supplied, one will be generated
        :return: string with error message if failed, uuid otherwise
        """

        if name is None:
            name = "stream-" + str(uuid4())[0:8]

        # save pipeline
        res1 = self.http_client.make_authed_request(
            self.service_uri + '/streams/collections', HttpMethod.POST, { "name": name }
        )

        pipeline_id = res1.get("id")
        if pipeline_id is None:
            return DtlError("Created response did not return an id")

        created_streams = []
        # add stream
        for stream in streams:
            res2 = self.http_client.make_authed_request(
                self.service_uri + '/streams/collections/' + pipeline_id + "/stream", HttpMethod.POST, stream._as_payload()
            )

            if isinstance(res2, DtlError):
                return res2
            
            stream_meta = _stream_metadata_from_payload(res2)
            if isinstance(stream_meta, DtlError):
                return stream_meta

            created_streams.append(stream_meta)

        return Pipeline(pipeline_id, name, created_streams)

    def update(self, pipeline_id: UUID, name: Optional[str] = None, streams: Optional[List[Stream]] = None) \
            -> Union[DtlError, Pipeline]:
        """
        Updates the pipeline

        :param pipeline_id: id of the pipeline to update
        :param name: new name of the pipeline
        :param streams: new set of streams for the pipeline (overrides the previous set)
        :return: Either an error message in a string or the pipeline
        """

        ref_pipeline = self.get(pipeline_id)
        if isinstance(ref_pipeline, DtlError):
            return DtlError("It looks like you are trying to update a pipeline that doesn't exist", ref_pipeline)

        if isinstance(name, str):

            res = self.http_client.make_authed_request(
                f"{self.service_uri}/streams/collections/{pipeline_id}", HttpMethod.PUT, {"name": name}
            )

            if isinstance(res, DtlError):
                return res

        if isinstance(streams, list):

            # We start by removing all the existing streams
            for stream in ref_pipeline.streams:
                res = self.http_client.make_authed_request(f"{self.service_uri}/streams/{stream.id}", HttpMethod.DELETE)

                if isinstance(res, DtlError):
                    return DtlError("Could not delete all previously existing streams, interrupting update", res)

            # Then we attach all the new ones
            for stream in streams:
                res = self.http_client.make_authed_request(
                    f"{self.service_uri}/streams/collections/{pipeline_id}/stream", HttpMethod.POST, stream._as_payload()
                )
                if isinstance(res, DtlError):
                    return DtlError("Could not add all the new streams to the pipeline, interrupting update", res)

        return self.get(pipeline_id)

    def schedule(self, pipeline_id: UUID, date: datetime) -> Union[DtlError, bool]:
        """
        Creates a job to be run at the given date

        :param pipeline_id: id of the stream to be run
        :param date: date at which to run the stream, expected to be localized
        :return: Either an error message in a string or the UUID for the new job
        """

        res = self.http_client.make_authed_request(
            self.service_uri + '/streams/collections/' + str(pipeline_id) + "/schedule",
            HttpMethod.POST,
            {"runDate": date.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}
        )

        if isinstance(res, DtlError):
            return res

        return True

    def run(self, workflow_id: UUID) -> Union[DtlError, bool]:
        """
        Runs the workflow right now + 2 secs

        :param workflow_id: id of the workflow to run
        :return:
        """

        return self.schedule(workflow_id, datetime.now() + timedelta(seconds=2))

    def list(self, page: int = 1, item_per_page: int = 25) -> Union[DtlError, List[Pipeline]]:
        """
        Retrieves a list of the available streams (pipelines)

        TODO pagination
        :param page: page to be retrieved
        :param item_per_page: number of items to be put in a page
        :return: Returns a List of all the available streams or an error message as a string
        """
        res = self.http_client.make_authed_request(self.service_uri + "/streams/collections", HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _parse_list(_pipeline_from_payload)(res)

    def get(self, pipeline_id: UUID) -> Union[DtlError, Pipeline]:
        """
        From the provided id, get the corresponding stream (pipeline)

        :param pipeline_id:
        :return:
        """
        res = self.http_client.make_authed_request(
            self.service_uri + "/streams/collections/" + str(pipeline_id), HttpMethod.GET)

        if isinstance(res, DtlError):
            return res

        return _pipeline_from_payload(res)

    def delete(self, pipeline_id: UUID) -> Union[DtlError, bool]:
        """
        Deletes the given stream (pipeline)

        :param pipeline_id: id of the stream (pipeline) to be deleted
        :return: true if successful, false otherwise
        """

        res = self.http_client.make_authed_request(
            self.service_uri + "/streams/collections/" + str(pipeline_id), HttpMethod.DELETE)

        if isinstance(res, DtlError):
            return res
        else:
            return True
