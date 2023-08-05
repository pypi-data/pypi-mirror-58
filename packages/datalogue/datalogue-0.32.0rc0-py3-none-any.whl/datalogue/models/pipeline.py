from typing import List, Union
from uuid import UUID
from datalogue.models.stream import Stream
from datalogue.utils import _parse_list
from datalogue.errors import DtlError


class StreamMetadata:
    def __init__(self, stream_id: UUID, is_ready: bool, stream: Stream):
        self.id = stream_id
        self.is_ready = is_ready
        self.stream = stream

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id},' \
               f' is_ready: {self.is_ready!r}, stream: {self.stream!r})'

    def _as_payload(self):
        base = dict()
        base["id"] = str(self.id)
        base["isReady"] = self.is_ready
        base["stream"] = self.stream._as_payload()
        return base


def _stream_metadata_from_payload(json: dict) -> Union[DtlError, StreamMetadata]:
    stream_id = json.get("id")
    if stream_id is None:
        return DtlError("'id' not defined in stream metadata")
    else:
        try:
            stream_id = UUID(stream_id)
        except ValueError:
            return DtlError("'id' is not a valid uuid")

    is_ready = json.get("isReady")
    if is_ready is None:
        is_ready = False

    stream = json.get("stream")
    if stream is None:
        return DtlError("'stream' needs to be defined in stream metadata payload")
    else:
        stream = Stream._from_payload(stream)
        if isinstance(stream, DtlError):
            return stream

    return StreamMetadata(stream_id, is_ready, stream)


class Pipeline:
    def __init__(self, pipeline_id: UUID, name: str, streams: List[StreamMetadata]):
        self.id = pipeline_id
        self.name = name
        self.streams = streams

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id}, name: {self.name!r}, streams: {self.streams!r})'

    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object with camelCase keys
        :return:
        """
        base = dict()
        base["id"] = str(self.id)
        base["name"] = self.name
        base["streams"] = list(map(lambda s: s._as_payload(), self.streams))
        return base


def _pipeline_from_payload(json: dict) -> Union[DtlError, Pipeline]:
    """
    Builds a Pipeline from a json dictionary

    :param json:
    :return: a string with the error message or the pipeline
    """

    pipeline_id = json.get("id")
    if pipeline_id is None:
        return DtlError("A Pipeline needs to have an 'id' property")
    else:
        try:
            pipeline_id = UUID(pipeline_id)
        except ValueError:
            return DtlError("The id field in the pipeline dictionary was not a valid UUID")

    name = json.get("name")
    if name is None:
        return DtlError("A Pipeline needs a 'name' field")
    else:
        if not isinstance(name, str):
            return DtlError("name field in the pipeline is expected to be a string")

    streams = json.get("streams")
    if streams is None:
        return DtlError("A Pipeline needs a 'streams' property")
    else:
        streams = _parse_list(_stream_metadata_from_payload)(json["streams"])
        if isinstance(streams, DtlError):
            return streams

    return Pipeline(pipeline_id, name, streams)
