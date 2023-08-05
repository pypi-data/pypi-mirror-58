from typing import TypeVar, List, Callable, Union, Dict, Type
from enum import Enum
from abc import abstractmethod, ABC

from datalogue.errors import DtlError

T = TypeVar('T')
Json = Union[Dict, str, int, List]


def _parse_list(parse_function: Callable[[Json], Union[DtlError, T]]) -> Callable[[List[Json]], Union[DtlError, List[T]]]:
    """
    Returns another function that can be used to parse a list of json with the specified parse function

    :param parse_function: function to be used for parsing
    :return:
    """
    def parse_concrete(objects: List[Json]) -> Union[DtlError, List[T]]:
        """
        Applies the parse function specified in the parent function to each element of the list of json

        :param objects: list to apply the parse function to
        :return:
        """
        parsed_list = []
        for obj in objects:
            parsed_obj = parse_function(obj)

            if isinstance(parsed_obj, DtlError):
                return parsed_obj
            else:
                parsed_list.append(parsed_obj)

        return parsed_list
    return parse_concrete


def _parse_string_list(objects: List[Json]) -> Union[DtlError, List[str]]:
    parsed_list = []

    for obj in objects:
        if isinstance(obj, str):
            parsed_list.append(obj)
        else:
            return DtlError("The following object is not a string: %s" % obj)

    return parsed_list


def not_implemented() -> NotImplemented:
    return NotImplemented


class SerializableStringEnum(Enum):

    @staticmethod
    def from_str(enum: Type['SerializableStringEnum']) -> Callable[[str], Union[DtlError, 'SerializableStringEnum']]:
        """
        Builds a function to parse the string enum `enum`
        :param enum: enum to create a parser for
        :return:
        """
        def inner_sanctum(s: str) -> Union[DtlError, 'SerializableStringEnum']:
            """
            Parses a string and returns the instance of the Enum it corresponds to or a string with an error message

            :param s: string to be parsed
            :return:
            """
            for blob_type in enum:
                if blob_type.value == s:
                    return blob_type

            return enum.parse_error(s)

        return inner_sanctum

    def __repr__(self):
        return f"{self._value_}"

    @staticmethod
    @abstractmethod
    def parse_error(s: str) -> DtlError:
        """
        Returns the error to be used if the parsing fails
        :return: string error
        """
        return NotImplemented
