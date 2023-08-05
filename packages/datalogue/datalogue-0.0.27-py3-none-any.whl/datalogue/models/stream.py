from typing import List, Union
from datalogue.models.datastore import DataStore, StoreDefinition, _store_definition_from_payload
from datalogue.models.transformations import Transformation, _transformation_from_payload
from datalogue.utils import _parse_list
from datalogue.errors import DtlError


class Pipeline:
    def __init__(self, transformations: List[Transformation], pipelines: List['Pipeline'],
                 target: Union[DataStore, StoreDefinition]):
        if isinstance(target, DataStore):
            target = target.definition

        self.transformations = transformations
        self.pipelines = pipelines
        self.target = target

    def __eq__(self, other: 'Pipeline'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> Union[DtlError, dict]:
        if self.target.store_id is None:
            return DtlError("Cannot serialize a pipeline with a target that was not saved to the database (id missing)")

        return {
            "transformations": list(map(lambda s: s._as_payload(), self.transformations)),
            "pipelines": list(map(lambda s: s._as_payload(), self.pipelines)),
            "target": self.target._as_payload()
        }


def _pipeline_from_payload(pipeline: dict) -> Union[DtlError, Pipeline]:
    """
    Builds a pipeline object from a dictionary,

    :param pipeline:
    :return: if fails returns a string with the error message
    """

    transformations = pipeline.get("transformations")
    if transformations is not None:
        transformations = _parse_list(_transformation_from_payload)(transformations)
        if isinstance(transformations, DtlError):
            return transformations
    else:
        transformations = list()

    pipelines = pipeline.get("pipelines")
    if pipelines is not None:
        pipelines = _parse_list(_pipeline_from_payload)(pipelines)
        if isinstance(pipelines, DtlError):
            return pipelines
    else:
        pipelines = list()

    target = pipeline.get("target")
    if target is None:
        return DtlError("Cannot have a pipeline without a 'target' property")
    else:
        target = _store_definition_from_payload(target)
        if isinstance(target, DtlError):
            return target

    return Pipeline(transformations, pipelines, target)


class Stream:
    def __init__(self, source: Union[StoreDefinition, DataStore], pipelines: List[Pipeline]):
        if isinstance(source, DataStore):
            source = source.definition

        self.source = source
        self.pipelines = pipelines

    def _as_payload(self):
        return {
            "source": self.source._as_payload(),
            "pipelines": list(map(lambda s: s._as_payload(), self.pipelines)),
        }


def stream_from_dict(json: dict) -> Union[DtlError, Stream]:
    return _stream_from_payload(json)


def _stream_from_payload(json: dict) -> Union[DtlError, Stream]:
    """
    Builds a Stream from a json Stream

    :param json:
    :return: if fails returns a string with the error message
    """
    source = json.get("source")
    if source is None:
        return DtlError("stream needs a source of data")
    else:
        source = _store_definition_from_payload(source)
        if isinstance(source, DtlError):
            return source

    pipelines = json.get("pipelines")
    if pipelines is None:
        return DtlError("streams needs a 'pipelines' property")
    else:
        pipelines = _parse_list(_pipeline_from_payload)(pipelines)
        if isinstance(pipelines, DtlError):
            return pipelines

    return Stream(source, pipelines)
