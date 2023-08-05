from typing import List, Union
from uuid import UUID
from datalogue.models.stream import Stream, _stream_from_payload
from datalogue.utils import _parse_list
from datalogue.errors import DtlError


class StreamMetadata:
    def __init__(self, stream_id: UUID, workflow_id: UUID, is_ready: bool, stream: Stream):
        self.id = stream_id
        self.workflow_id = workflow_id
        self.is_ready = is_ready
        self.stream = stream


def _stream_metadata_from_payload(json: dict) -> Union[DtlError, StreamMetadata]:
    stream_id = json.get("id")
    if stream_id is None:
        return DtlError("'id' not defined in stream metadata")
    else:
        try:
            stream_id = UUID(stream_id)
        except ValueError:
            return DtlError("'id' is not a valid uuid")

    workflow_id = json.get("workflowId")
    if workflow_id is None:
        return DtlError("'workflow_id' not defined in stream metadata")
    else:
        try:
            workflow_id = UUID(workflow_id)
        except ValueError:
            return DtlError("'workflow_id' is not a valid uuid")

    is_ready = json.get("isReady")
    if is_ready is None:
        is_ready = False

    stream = json.get("stream")
    if stream is None:
        return DtlError("'stream' needs to be defined in stream metadata payload")
    else:
        stream = _stream_from_payload(stream)
        if isinstance(stream, DtlError):
            return stream

    return StreamMetadata(stream_id, workflow_id, is_ready, stream)


class Workflow:
    def __init__(self, workflow_id: UUID, name: str, streams: List[StreamMetadata]):
        self.id = workflow_id
        self.name = name
        self.streams = streams


def _workflow_from_payload(json: dict) -> Union[DtlError, Workflow]:
    """
    Builds a Workflow from a json dictionary

    :param json:
    :return: a string with the error message or the workflow
    """

    workflow_id = json.get("id")
    if workflow_id is None:
        return DtlError("A Workflow needs to have an 'id' property")
    else:
        try:
            workflow_id = UUID(workflow_id)
        except ValueError:
            return DtlError("The id field in the workflow dictionary was not a valid UUID")

    name = json.get("name")
    if name is None:
        return DtlError("A Workflow needs a 'name' field")
    else:
        if not isinstance(name, str):
            return DtlError("name field in the workflow is expected to be a string")

    streams = json.get("streams")
    if streams is None:
        return DtlError("A Workflow needs a 'streams' property")
    else:
        streams = _parse_list(_stream_metadata_from_payload)(json["streams"])
        if isinstance(streams, DtlError):
            return streams

    return Workflow(workflow_id, name, streams)
