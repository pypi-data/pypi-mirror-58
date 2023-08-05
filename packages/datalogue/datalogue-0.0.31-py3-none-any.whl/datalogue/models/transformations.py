from typing import List, Union, Optional
from datalogue.errors import DtlError
from datalogue.utils import _parse_string_list, _parse_list
from datalogue.models.datastore import DataStore, _store_definition_from_payload, StoreDefinition
import abc


class Transformation(abc.ABC):

    type_field = "type"

    def __init__(self, transformation_type: str):
        self.type = transformation_type
        super().__init__()

    def _base_payload(self) -> dict:
        return dict([(Transformation.type_field, self.type)])

    @abc.abstractmethod
    def _as_payload(self) -> dict:
        """
        Represents the transformation in its dictionary construction

        :return:
        """


def _array_from_dict(json: dict, transformation_type: str, array_field_key: str) -> Union[DtlError, List[str]]:
    """
    Generic method to extract an array from a json transformation dictionary

    :param json: dictionary built from json
    :param transformation_type: type of the transformation
    :param array_field_key: key at which the array is
    :return:
    """
    if json.get(Transformation.type_field) != transformation_type:
        return DtlError("Dictionary input is not of type %s" % transformation_type)

    array_field = json.get(array_field_key)
    if array_field is None:
        return DtlError("'%s' is missing from the json transformation" % array_field_key)

    array = _parse_string_list(array_field)

    if isinstance(array, DtlError):
        return array

    return array

#############################################################################################
#                                    ADG Transformations
#############################################################################################


class Split(Transformation):
    """
    Splits the tree into list of trees. Each new tree is formed by the root node found at the given path
    and all its children recursively.
    """

    type_str = "Split"

    def __init__(self, path: List[str]):
        Transformation.__init__(self, Split.type_str)
        self.path = path

    def __eq__(self, other: 'Split'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        return base


def _split_transformation_from_payload(json: dict) -> Union[DtlError, Split]:
    array = _array_from_dict(json, Split.type_str, "path")
    if isinstance(array, DtlError):
        return array

    return Split(array)


class Flatten(Transformation):
    """
    Places all leaf nodes in the tree as children of the root node. All intermediate nodes are removed. Labels
    of leaf nodes are updated to reflect the materialized path they used to have with the delimiter parameter.
    """

    type_str = "Flatten"

    def __init__(self, delimiter: str):
        Transformation.__init__(self, Flatten.type_str)
        self.delimiter = delimiter

    def __eq__(self, other: 'Flatten'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["delimiter"] = self.delimiter
        return base


def _flatten_transformation_from_payload(json: dict) -> Union[DtlError, Flatten]:
    if json.get(Transformation.type_field) != Flatten.type_str:
        return DtlError("Dictionary input is not of type %s" % Flatten.type_str)

    path_field = json.get("delimiter")
    if path_field is None:
        return DtlError("delimiter is missing from the json transformation")

    if not isinstance(path_field, str):
        return DtlError("delimiter should be a string")

    return Flatten(path_field)


class MapFilterNotByLabel(Transformation):
    """
    Removes data nodes with given labels.
    """

    type_str = "MapFilterNotByLabel"

    def __init__(self, labels: List[str]):
        Transformation.__init__(self, MapFilterNotByLabel.type_str)
        self.labels = labels

    def __eq__(self, other: 'MapFilterNotByLabel'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["labels"] = self.labels
        return base


def _map_filter_not_by_label_from_payload(json: dict) -> Union[DtlError, MapFilterNotByLabel]:

    array = _array_from_dict(json, MapFilterNotByLabel.type_str, "labels")
    if isinstance(array, DtlError):
        return array

    return MapFilterNotByLabel(array)


class MapFilterByClass(Transformation):
    """
    Keeps data nodes which are classified as one of the given classes.
    """

    type_str = "MapFilterByClass"

    def __init__(self, classes: List[str]):
        Transformation.__init__(self, MapFilterByClass.type_str)
        self.classes = classes

    def __eq__(self, other: 'MapFilterByClass'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["classes"] = self.classes
        return base


def _map_filter_by_class_from_payload(json: dict) -> Union[DtlError, MapFilterByClass]:
    array = _array_from_dict(json, MapFilterByClass.type_str, "classes")
    if isinstance(array, DtlError):
        return array

    return MapFilterByClass(array)


class MapFilterByPath(Transformation):
    """
     Keeps data nodes by given materialized paths (path from root to node). Materialized path is encoded as list of labels.
    """
    type_str = "MapFilterByPath"

    def __init__(self, paths: List[List[str]]):
        Transformation.__init__(self, MapFilterByPath.type_str)
        self.paths = paths

    def __eq__(self, other: 'MapFilterByPath'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["paths"] = self.paths
        return base


def _map_filter_by_path_from_payload(json: dict) -> Union[DtlError, MapFilterByPath]:
    if json.get(Transformation.type_field) != MapFilterByPath.type_str:
        return DtlError("Dictionary input is not of type %s" % MapFilterByPath.type_str)

    array_field = json.get("paths")
    if array_field is None:
        return DtlError("'paths' is missing from the json transformation")

    array = _parse_list(_parse_string_list)(array_field)

    if isinstance(array, DtlError):
        return array

    return MapFilterByPath(array)


class ReplaceLabel(Transformation):
    """
    Finds all nodes at the given path and replaces their label with the given one.
    """
    type_str = "ReplaceLabel"

    def __init__(self, path: List[str], replacement: str):
        Transformation.__init__(self, ReplaceLabel.type_str)
        self.path = path
        self.replacement = replacement

    def __eq__(self, other: 'ReplaceLabel'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["replacement"] = self.replacement
        return base


def _replace_label_from_payload(json: dict) -> Union[DtlError, ReplaceLabel]:
    array = _array_from_dict(json, ReplaceLabel.type_str, "path")
    if isinstance(array, DtlError):
        return array

    replacement = json.get("replacement")
    if not isinstance(replacement, str):
        return DtlError("replacement field is not a string in %s transformation" % ReplaceLabel.type_str)

    return ReplaceLabel(array, replacement)


class ReplaceValue(Transformation):
    """
    Finds all nodes at the given path and replaces their value with the given one.
    """
    type_str = "ReplaceValue"

    def __init__(self, path: List[str], replacement: str):
        Transformation.__init__(self, ReplaceValue.type_str)
        self.path = path
        self.replacement = replacement

    def __eq__(self, other: 'ReplaceValue'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["replacement"] = self.replacement
        return base


def _replace_value_from_payload(json: dict) -> Union[DtlError, ReplaceValue]:
    array = _array_from_dict(json, ReplaceValue.type_str, "path")
    if isinstance(array, DtlError):
        return array

    replacement = json.get("replacement")
    if not isinstance(replacement, str):
        return DtlError("replacement field is not a string in %s transformation" % ReplaceValue.type_str)

    return ReplaceValue(array, replacement)


class ReplaceValueByRegex(Transformation):
    """
    Finds all nodes at the given path and replaces their value with the given one.
    """
    type_str = "ReplaceValueByRegex"

    def __init__(self, path: List[str], regex: str, replacement: str):
        Transformation.__init__(self, ReplaceValueByRegex.type_str)
        self.path = path
        self.replacement = replacement
        self.regex = regex

    def __eq__(self, other: 'ReplaceValueByRegex'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["replacement"] = self.replacement
        base["regex"] = self.regex
        return base


def _replace_value_by_regex_from_payload(json: dict) -> Union[DtlError, ReplaceValueByRegex]:
    array = _array_from_dict(json, ReplaceValueByRegex.type_str, "path")
    if isinstance(array, DtlError):
        return array

    replacement = json.get("replacement")
    if not isinstance(replacement, str):
        return DtlError("replacement field is not a string in %s transformation" % ReplaceValueByRegex.type_str)

    regex = json.get("regex")
    if not isinstance(regex, str):
        return DtlError("regex field is not a string in %s transformation" % ReplaceValueByRegex.type_str)

    return ReplaceValueByRegex(array, regex, replacement)


class SplitValueByRegex(Transformation):
    """
    Finds all nodes at the given path which have at least one match of the given regex in their value and splits
    them into several nodes with the same label and matched substring as a value.
    """
    type_str = "SplitValueByRegex"

    def __init__(self, path: List[str], regex: str):
        Transformation.__init__(self, SplitValueByRegex.type_str)
        self.path = path
        self.regex = regex

    def __eq__(self, other: 'SplitValueByRegex'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["regex"] = self.regex
        return base


def _split_value_by_regex_from_payload(json: dict) -> Union[DtlError, SplitValueByRegex]:
    array = _array_from_dict(json, SplitValueByRegex.type_str, "path")
    if isinstance(array, DtlError):
        return array

    regex = json.get("regex")
    if not isinstance(regex, str):
        return DtlError("regex field is not a string in %s transformation" % ReplaceValue.type_str)

    return SplitValueByRegex(array, regex)


class Move(Transformation):
    """
    Finds all nodes at the given path and moves them as children of a new parent identified by the given to path.
    """
    type_str = "Move"

    def __init__(self, path: List[str], to: List[str]):
        Transformation.__init__(self, Move.type_str)
        self.path = path
        self.to = to

    def __eq__(self, other: 'Move'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["to"] = self.to
        return base


def _move_from_payload(json: dict) -> Union[DtlError, Move]:
    path = _array_from_dict(json, Move.type_str, "path")
    if isinstance(path, DtlError):
        return path

    to = _array_from_dict(json, Move.type_str, "to")
    if isinstance(to, DtlError):
        return to

    return Move(path, to)


class Copy(Transformation):
    """
    Finds all nodes at the given path and copies them as children of all nodes identified by the given to path.
    """
    type_str = "Copy"

    def __init__(self, path: List[str], to: List[str]):
        Transformation.__init__(self, Copy.type_str)
        self.path = path
        self.to = to

    def __eq__(self, other: 'Copy'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["to"] = self.to
        return base


def _copy_from_payload(json: dict) -> Union[DtlError, Copy]:
    path = _array_from_dict(json, Copy.type_str, "path")
    if isinstance(path, DtlError):
        return path

    to = _array_from_dict(json, Copy.type_str, "to")
    if isinstance(to, DtlError):
        return to

    return Copy(path, to)


class CopyWithNewLabel(Transformation):
    """
    Finds all nodes at the given path, relabels them as label and copies them as children of all nodes
    identified by the given to path.
    """
    type_str = "CopyWithNewLabel"

    def __init__(self, path: List[str], to: List[str], label: str):
        Transformation.__init__(self, CopyWithNewLabel.type_str)
        self.path = path
        self.to = to
        self.label = label

    def __eq__(self, other: 'CopyWithNewLabel'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["path"] = self.path
        base["to"] = self.to
        base["label"] = self.label
        return base


def _copy_with_new_label_from_payload(json: dict) -> Union[DtlError, CopyWithNewLabel]:
    path = _array_from_dict(json, CopyWithNewLabel.type_str, "path")
    if isinstance(path, DtlError):
        return path

    to = _array_from_dict(json, CopyWithNewLabel.type_str, "to")
    if isinstance(to, DtlError):
        return to

    label = json.get("label")
    if not isinstance(label, str):
        return DtlError("label should be a string")

    return CopyWithNewLabel(path, to, label)


class RemoveEmptyBranches(Transformation):
    """
    Filters out data nodes which have no value. This operation is recursive: if all children of parent node are
     removed, the parent node is also removed.
    """
    type_str = "RemoveEmptyBranches"

    def __init__(self):
        Transformation.__init__(self, RemoveEmptyBranches.type_str)

    def __eq__(self, other: 'RemoveEmptyBranches'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        return self._base_payload()


def _remove_empty_branches_from_payload(json: dict) -> Union[DtlError, RemoveEmptyBranches]:

    if json.get(Transformation.type_field) != RemoveEmptyBranches.type_str:
        return DtlError("Dictionary input is not of type %s" % RemoveEmptyBranches.type_str)

    return RemoveEmptyBranches()


#############################################################################################
#                                    Stream Transformations
#############################################################################################

class ElementCountSelection(Transformation):
    """
    Takes specified number of items and ignores the rest.
    """
    type_str = "ElementCountSelection"

    def __init__(self, count: int):
        Transformation.__init__(self, ElementCountSelection.type_str)
        self.count = count

    def __eq__(self, other: 'ElementCountSelection'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["count"] = self.count
        return base


def _element_count_selection_from_payload(json: dict) -> Union[DtlError, ElementCountSelection]:

    if json.get(Transformation.type_field) != ElementCountSelection.type_str:
        return DtlError("Dictionary input is not of type %s" % ElementCountSelection.type_str)

    count = json.get("count")
    if not isinstance(count, int):
        return DtlError("%s needs a count property that is an int")

    return ElementCountSelection(count)


class PathAndValue:
    """
    Represents the associated tuple of a path with a value
    """
    def __init__(self, path: List[str], value: str):
        self.path = path
        self.value = value

    def __eq__(self, other: 'PathAndValue'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        return {"path": self.path, "value": self.value}


def _path_and_value_from_payload(json: dict) -> Union[DtlError, PathAndValue]:
    path = json.get("path")
    if path is None:
        return DtlError("path needs to be defined for %s" % str(json))

    value = json.get("value")
    if value is None:
        return DtlError("value needs to be defined for %s" % str(json))

    return PathAndValue(path, value)


class FilterByPathAndValue(Transformation):
    """
    Filters the stream and keeps items that have at least one matched node and value from the given set
     of node path and value pairs.
    """
    type_str = "FilterByPathAndValue"

    def __init__(self, paths_and_values: List[PathAndValue]):
        Transformation.__init__(self, FilterByPathAndValue.type_str)
        self.paths_and_values = paths_and_values

    def __eq__(self, other: 'FilterByPathAndValue'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["paths"] = list(map(lambda c: c._as_payload(), self.paths_and_values))
        return base


def _filter_by_path_and_value_from_payload(json: dict) -> Union[DtlError, FilterByPathAndValue]:

    if json.get(Transformation.type_field) != FilterByPathAndValue.type_str:
        return DtlError("Dictionary input is not of type %s" % FilterByPathAndValue.type_str)

    array_field = json.get("paths")
    if array_field is None:
        return DtlError("'paths' is missing from the json transformation")

    parsed_list = _parse_list(_path_and_value_from_payload)(array_field)
    if isinstance(parsed_list, DtlError):
        return parsed_list

    return FilterByPathAndValue(parsed_list)


class FilterByClass(Transformation):
    """
    Filters the stream and keeps items that have nodes which are classified as one of the given classes.
    """

    type_str = "FilterByClass"

    def __init__(self, classes: List[str]):
        Transformation.__init__(self, FilterByClass.type_str)
        self.classes = classes

    def __eq__(self, other: 'FilterByClass'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["classes"] = self.classes
        return base


def _filter_by_class_from_payload(json: dict) -> Union[DtlError, FilterByClass]:
    array = _array_from_dict(json, FilterByClass.type_str, "classes")
    if isinstance(array, DtlError):
        return array

    return FilterByClass(array)


#############################################################################################
#                                    Joins Transformations
#############################################################################################

class InnerJoin(Transformation):
    """
    Joins current dataset with another dataset by matched fields using inner join logic. For example,
    if dataset S1 with fields A and B is joined with dataset S2 with fields C and D where S1.B == S2.D,
    then resulting dataset S1' will have fields A, B, C and D.

    Nodes in ADG are referenced by their materialized paths, encoded as array of labels.
    transformations (optional) can be used to transform the source before it's being joined. Any transformations are allowed.
    The syntax is inspired by SQL join statement, compare SQL and JSON versions below.
    SELECT ... FROM A INNER JOIN B ON A.name = B.related_name
    """

    type_str = "InnerJoin"

    def __init__(self, source: Union[StoreDefinition, DataStore], transformations: List[Transformation], on: List[str],
                 equals: List[str]):
        Transformation.__init__(self, InnerJoin.type_str)

        if isinstance(source, DataStore):
            source = source.definition

        self.source = source
        self.transformations = transformations
        self.on = on
        self.equals = equals

    def __eq__(self, other: 'InnerJoin'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["source"] = self.source._as_payload()
        base["transformations"] = list(map(lambda t: t._as_payload(), self.transformations))
        base["on"] = self.on
        base["equals"] = self.equals
        return base


class OuterJoin(Transformation):
    """
    The version of join that uses outer join logic. SELECT ... FROM A OUTER JOIN C ON A.name = C.related_name
    """

    type_str = "OuterJoin"

    def __init__(self, source: Union[StoreDefinition, DataStore], transformations: List[Transformation], on: List[str],
                 equals: List[str]):
        Transformation.__init__(self, OuterJoin.type_str)

        if isinstance(source, DataStore):
            source = source.definition

        self.source = source
        self.transformations = transformations
        self.on = on
        self.equals = equals

    def __eq__(self, other: 'OuterJoin'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()
        base["source"] = self.source._as_payload()
        base["transformations"] = list(map(lambda t: t._as_payload(), self.transformations))
        base["on"] = self.on
        base["equals"] = self.equals
        return base


def _join_from_payload(json: dict, join_type: str) -> Union[DtlError, OuterJoin, InnerJoin]:
    print(join_type)
    print(json.get(Transformation.type_field))
    if json.get(Transformation.type_field) != join_type:
        return DtlError("Dictionary input is not of type " % join_type)

    print("rtest")

    source_field = json.get("source")
    if source_field is None:
        return DtlError("'%s' needs a source field" % join_type)

    source = _store_definition_from_payload(source_field)
    if isinstance(source, DtlError):
        return source

    transformations_field = json.get("transformations")
    if isinstance(transformations_field, List):
        transformations = _parse_list(_transformation_from_payload)(transformations_field)
        if isinstance(transformations, DtlError):
            return transformations
    else:
        transformations = list()

    on = _array_from_dict(json, join_type, "on")
    if isinstance(on, DtlError):
        return on

    equals = _array_from_dict(json, join_type, "equals")
    if isinstance(equals, DtlError):
        return equals

    if join_type == InnerJoin.type_str:
        return InnerJoin(source, transformations, on, equals)
    else:
        return OuterJoin(source, transformations, on, equals)


def _inner_join_from_payload(json: dict) -> Union[str, InnerJoin]:
    return _join_from_payload(json, InnerJoin.type_str)


def _outer_join_from_payload(json: dict) -> Union[str, OuterJoin]:
    return _join_from_payload(json, OuterJoin.type_str)


#############################################################################################
#                                    ML Transformations
#############################################################################################


class ReplaceClass:

    threshold_key = "threshold"
    new_class_key = "newClass"

    def __init__(self, threshold: float, new_class: str):
        self.threshold = threshold
        self.new_class = new_class

    def __eq__(self, other: 'ReplaceClass'):
        if isinstance(self, other.__class__):
            return self.threshold == other.threshold and self.new_class == other.new_class
        return False


class Classify(Transformation):
    """
    Classify: Runs all data nodes through the ontology detection service and passes the classification
     results to the next stage.
    """

    type_str = "Classify"

    use_context_type = "UseContext"
    include_classes_type = "CreateClassNodes"
    include_scores_type = "CreateScoreNodes"
    replace_class_type = "ReplaceClass"
    audit_param_type = "AuditParams"
    dataset_name_key = "datasetName"

    def __init__(self, paths: Optional[List[List[str]]] = None, use_context: bool = False, include_classes: bool = False,
                 include_scores: bool = False, replace_class: Optional[ReplaceClass] = None, dataset_name: Optional[str] = None):
        """
        Builds a classification transformation

        :param paths: classifies specified nodes only if provided, or all nodes if omitted.
        :param use_context: uses the CBC model instead of CFC model. Context is the node label.
        :param include_classes: augments resulting ADGs with xyz_#DTL_class nodes containing ontology class for
                corresponding xyz nodes.
        :param include_scores:  augments resulting ADGs with xyz_#DTL_score nodes containing classification score
                for corresponding xyz nodes.
        :param replace_class: class in the classification results is replaced by the given newClass if the score is
                below the given threshold. The default value for the new class is unknown.
        :param dataset_name: the name of the dataset for the Audit. Specifying the name allows to easily
                find classification results in the Audit view.
        """
        Transformation.__init__(self, Classify.type_str)
        self.paths = paths
        self.use_context = use_context
        self.include_classes = include_classes
        self.include_scores = include_scores
        self.replace_class = replace_class
        self.dataset_name = dataset_name

    def __eq__(self, other: 'Classify'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()

        if self.paths is not None:
            base["paths"] = self.paths
        options = []

        if self.use_context:
            options.append({self.type_field: self.use_context_type})
        if self.include_classes:
            options.append({self.type_field: self.include_classes_type})
        if self.include_scores:
            options.append({self.type_field: self.include_scores_type})
        if self.replace_class is not None:
            options.append({
                self.type_field: self.replace_class_type,
                ReplaceClass.threshold_key: self.replace_class.threshold,
                ReplaceClass.new_class_key: self.replace_class.new_class
            })
        if self.dataset_name is not None:
            options.append({
                self.type_field: self.audit_param_type,
                Classify.dataset_name_key: self.dataset_name,
            })

        if len(options) > 0:
            base["options"] = options

        return base


def _classify_from_payload(json: dict) -> Union[DtlError, Classify]:
    if json.get(Transformation.type_field) != Classify.type_str:
        return DtlError("Dictionary input is not of type %s" % Classify.type_str)

    paths = json.get("paths")
    if paths is not None:
        paths = _parse_list(_parse_string_list)(paths)

    options = json.get("options")
    use_context = False
    include_classes = False
    include_score = False
    replace_class = None
    dataset_name = None

    if isinstance(options, List):
        for option in options:
            if option.get(Transformation.type_field) == Classify.use_context_type:
                use_context = True
                continue

            if option.get(Transformation.type_field) == Classify.include_classes_type:
                include_classes = True
                continue

            if option.get(Transformation.type_field) == Classify.include_scores_type:
                include_score = True
                continue

            if option.get(Transformation.type_field) == Classify.replace_class_type:
                threshold = option.get(ReplaceClass.threshold_key)
                new_class = option.get(ReplaceClass.new_class_key)

                if threshold is not None and new_class is not None:
                    replace_class = ReplaceClass(threshold, new_class)
                    continue

            if option.get(Transformation.type_field) == Classify.audit_param_type:
                dataset_name = option.get(Classify.dataset_name_key)

    return Classify(paths, use_context, include_classes, include_score, replace_class, dataset_name)


# Left todo finish transformations


# RecognizeEntities: Runs all data nodes through the entity recognition service using NER model and passes the classification results to the next stage. Since entity recognition process goes through the value of the node and analyzes individual tokens, one node may have several classification tags attached to it.
# CreateClassNodes, augments resulting ADGs with nodes containing found entities and their classes.
# CreateScoreNodes, augments resulting ADGs with nodes containing found entities and their classification scores.
# {
#     "type": "RecognizeEntities",
#     "options": [
#         {
#             "type": "CreateClassNodes"
#         },
#         {
#             "type": "CreateScoreNodes"
#         }
#     ]
# }
class RecognizeEntities(Transformation):
    """
    RecognizeEntities: Runs all data nodes through the entity recognition service using NER model and passes the classification results to the next stage. Since entity recognition process goes through the value of the node and analyzes individual tokens, one node may have several classification tags attached to it.
    """

    type_str = "RecognizeEntities"

    include_classes_type = "CreateClassNodes"
    include_scores_type = "CreateScoreNodes"

    def __init__(self, include_classes: bool = False, include_scores: bool = False):
        """
        Builds an entity recognition transformation

        :param include_classes: augments resulting ADGs with xyz_#DTL_class nodes containing ontology class for corresponding xyz nodes.
        :param include_scores:  augments resulting ADGs with xyz_#DTL_score nodes containing classification score for corresponding xyz nodes.
        """
        Transformation.__init__(self, RecognizeEntities.type_str)
        self.include_classes = include_classes
        self.include_scores = include_scores

    def __eq__(self, other: 'RecognizeEntities'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()

        options = []

        if self.include_classes:
            options.append({self.type_field: self.include_classes_type})
        if self.include_scores:
            options.append({self.type_field: self.include_scores_type})

        if len(options) > 0:
            base["options"] = options

        return base


class StandardizeDates(Transformation):
    type_str = "StandardizeDates"

    include_new_nodes_type = "CreateNewNodes"

    def __init__(self, paths: Optional[List[List[str]]] = None, include_new_nodes: bool = False):
        Transformation.__init__(self, StandardizeDates.type_str)
        self.paths = paths
        self.include_new_nodes = include_new_nodes

    def __eq__(self, other: 'StandardizeDates'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _as_payload(self) -> dict:
        base = self._base_payload()

        if self.paths is not None:
            base["paths"] = self.paths

        options = []
        if self.include_new_nodes:
            options.append({self.type_field: self.include_new_nodes_type})

        if len(options) > 0:
            base["options"] = options

        return base


def _entity_recognition_from_payload(json: dict) -> Union[DtlError, RecognizeEntities]:
    if json.get(Transformation.type_field) != RecognizeEntities.type_str:
        return DtlError("Dictionary input is not of type %s" % RecognizeEntities.type_str)

    options = json.get("options")
    include_classes = False
    include_score = False

    if isinstance(options, List):
        for option in options:

            if option.get(Transformation.type_field) == RecognizeEntities.include_classes_type:
                include_classes = True
                continue

            if option.get(Transformation.type_field) == RecognizeEntities.include_scores_type:
                include_score = True
                continue

    return RecognizeEntities(include_classes, include_score)


def _standardize_dates_from_payload(json: dict) -> Union[DtlError, StandardizeDates]:
    if json.get(Transformation.type_field) != StandardizeDates.type_str:
        return DtlError("Dictionary input is not of type %s" % StandardizeDates.type_str)

    paths = json.get("paths")
    if paths is not None:
        paths = _parse_list(_parse_string_list)(paths)

    options = json.get("options")
    include_new_nodes = False

    if isinstance(options, List) and len(options) > 0 and (options[0].get(Transformation.type_field) == StandardizeDates.include_new_nodes_type):
        include_new_nodes = True

    return StandardizeDates(paths, include_new_nodes)

# ParseAddresses (automatic): Requires Classify. Runs all data nodes classified as being address through the address parsing service and augments resulting ADGs with nodes containing parts of the address: street_address, zip_code, city etc. This transformation has to be specified after Classify for the address nodes to be detected first.
# [{
#     "type": "Classify"
# },
#     {
#         "type": "ParseAddresses"
#     }]
# ParseAddresses (manual): Runs specified data nodes through the address parsing service and augments resulting ADGs with nodes containing parts of the address: street_address, zip_code, city etc. Nodes in ADG are referenced by their materialized paths, encoded as array of labels.
# {
#     "type": "ParseAddresses",
#     "paths": [ ["root", "business_address"], ["root", "customer", "address"] ]
# }
# StandardizeDates (automatic): Requires Classify. Runs all data nodes classified as being date through the date format service and updates the values with standard date presentation. This transformation has to be specified after Classify for the date nodes to be detected first.
# [{
#     "type": "Classify"
# },
#     {
#         "type": "StandardizeDates"
#     }]
# StandardizeDates (manual): Runs specified data nodes through the date format service and updates the values with standard date presentation. Nodes in ADG are referenced by their materialized paths, encoded as array of labels.
# {
#     "type": "StandardizeDates",
#     "paths": [ ["root", "birthday"], ["root", "purchase", "date"] ]
# }
# StandardizeDates has the following options:
# CreateNewNodes, does not update nodes with new values but creates new nodes labeled DTL_standardized_date besides the original ones to hold the new values.
# {
#     "type": "StandardizeDates",
#     "options": [
#         {
#             "type": "CreateNewNodes"
#         }
#     ]
# }
# Segment: Requires Classify. Uses the results of classification to find groups of nodes classified according to provided tags. The group is formed if there is at least one node for each provided tag. When there are enough nodes to form multiple groups, the nodes are included by proximity to each other in the tree (usually via common parent). The result of this transformation is a list of ADGs, each containing one group of nodes. Additionally node labels are replaced with the corresponding classification tags.
# [{
#     "type": "Classify"
# },
#     {
#         "type": "Segment",
#         "tags": ["name", "address", "account"]
#     }]


_transformations = dict([
    (Split.type_str, _split_transformation_from_payload),
    (Flatten.type_str, _flatten_transformation_from_payload),
    (MapFilterNotByLabel.type_str, _map_filter_not_by_label_from_payload),
    (MapFilterByClass.type_str, _map_filter_by_class_from_payload),
    (MapFilterByPath.type_str, _map_filter_by_path_from_payload),
    (ReplaceLabel.type_str, _replace_label_from_payload),
    (ReplaceValue.type_str, _replace_value_from_payload),
    (ReplaceValueByRegex.type_str, _replace_value_by_regex_from_payload),
    (SplitValueByRegex.type_str, _split_value_by_regex_from_payload),
    (Move.type_str, _move_from_payload),
    (Copy.type_str, _copy_from_payload),
    (CopyWithNewLabel.type_str, _copy_with_new_label_from_payload),
    (RemoveEmptyBranches.type_str, _remove_empty_branches_from_payload),
    (ElementCountSelection.type_str, _element_count_selection_from_payload),
    (FilterByPathAndValue.type_str, _filter_by_path_and_value_from_payload),
    (FilterByClass.type_str, _filter_by_class_from_payload),
    (InnerJoin.type_str, _inner_join_from_payload),
    (OuterJoin.type_str, _outer_join_from_payload),
    (Classify.type_str, _classify_from_payload),
    (StandardizeDates.type_str, _standardize_dates_from_payload),
    (RecognizeEntities.type_str, _entity_recognition_from_payload)
])


def _transformation_from_payload(json: dict) -> Union[DtlError, Transformation]:
    type_field = json.get(Transformation.type_field)
    if type_field is None:
        return DtlError("The json object doesn't have a '%s' property" % Transformation.type_field)

    parsing_function = _transformations.get(type_field)
    if parsing_function is None:
        return DtlError("Looks like '%s' transformation is not handled by the SDK" % type_field)

    return parsing_function(json)
