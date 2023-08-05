from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union
from uuid import UUID

from datalogue.errors import _enum_parse_error, DtlError
from datalogue.utils import _parse_list, _parse_string_list, SerializableStringEnum


class StoreType(SerializableStringEnum):
    S3 = "S3"
    GCS = "GCS"
    AzureStorage = "AzureStorage"
    JDBC = "JDBC"
    Mongo = "Mongo"
    HttpResource = "HttpResource"
    Socrata = "Socrata"
    FileSystem = "FileSystem"
    FileUpload = "FileUpload"
    Void = "Void"

    @staticmethod
    def parse_error(s: str) -> DtlError:
        return DtlError(_enum_parse_error("store type", s))


def store_type_from_str(string: str) -> Union[DtlError, StoreType]:
    return SerializableStringEnum.from_str(StoreType)(string)


class FileFormat(SerializableStringEnum):
    Json = "Json"
    Csv = "Csv"
    Text = "Text"
    Xml = "Xml"
    Html = "Html"
    Excel = "Excel"

    @staticmethod
    def parse_error(s: str) -> DtlError:
        return DtlError(_enum_parse_error("file format", s))


def file_format_from_str(string: str) -> Union[DtlError, FileFormat]:
    return SerializableStringEnum.from_str(FileFormat)(string)


class StoreDefinition(ABC):
    type_field = "type"
    id_field = "_id"

    def __init__(self, definition_type: StoreType, store_id: Optional[UUID] = None):
        self.type = definition_type
        self.store_id = store_id
        super().__init__()

    def __eq__(self, other: 'StoreDefinition'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def _base_payload(self) -> dict:
        base = [(StoreDefinition.type_field, self.type.value)]
        if self.store_id is not None:
            base.append((StoreDefinition.id_field, str(self.store_id)))
        return dict(base)

    @abstractmethod
    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object
        :return:
        """
        pass


class Cell:
    """
        Describes a cell in html table
    """

    def __init__(self, label: str, span: int, index: int, total: int):
        """
        Builds a cell

        :param label: text to display
        :param span: the html column span attribute
        :param index: index of this cell in the row
        :param total: total number of cells in the row
        """
        self.label = label
        self.span = span
        self.index = index
        self.total = total

    def __repr__(self):
        return f"{self.__class__.__name__}(label: {self.label!r}, span: {self.span!r}, \
                index: {self.index!r}, total: {self.total!r})"


def _cell_from_payload(json: dict) -> Union[DtlError, Cell]:
    label = json.get("label")
    if label is None:
        return DtlError("Cell has to have a 'label' key")

    span = json.get("span")
    if span is None:
        return DtlError("Cell has to have a 'span' key")

    index = json.get("index")
    if index is None:
        return DtlError("Cell has to have an 'index' key")

    total = json.get("total")
    if total is None:
        return DtlError("Cell has to have a 'total' key")

    return Cell(label, span, index, total)


class DataStore:
    """
    Represents a pointer to a resource
    """

    def __init__(self, name: str, definition: StoreDefinition, credentials_id: Optional[UUID] = None,
                 alias: Optional[str] = None, store_id: Optional[UUID] = None,
                 samples: Optional[List[List[Cell]]] = None, schema: Optional[List[List[Cell]]] = None,
                 schema_paths: Optional[List[List[str]]] = None
                 ):
        """
        Builds a pointer to a data store

        :param name: name of the pointer
        :param alias: unique alias accross the organization for the pointer
        :param definition: definition on how to access the data
        :param credentials_id: reference to the credentials to access the data
        :param store_id: defined if the object was persisted, otherwise None
        :param samples: list of samples that were found in the data source
        :param schema: schema of the data source put into a matrix
        :param schema_paths: TODO find out what that is
        """
        self.id = store_id
        self.name = name
        self.alias = alias
        self.definition = definition
        self.definition.store_id = store_id
        self.credentials_id = credentials_id
        self.schema = schema
        self.samples = samples
        self.schema_paths = schema_paths

    def __eq__(self, other: 'DataStore'):
        if isinstance(self, other.__class__):
            return self._as_payload() == other._as_payload()
        return False

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id}, name: {self.name!r}, alias: {self.alias!r}, ' \
               f'credentials_id: {self.credentials_id}, definition: {self.definition!r}, schema: {self.schema!r}, ' \
               f'samples: {self.samples!r}, schema_paths: {self.schema_paths!r})'

    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object
        :return:
        """
        base = {
            "name": self.name,
            "gate": self.definition._as_payload(),
        }
        if self.id is not None:
            base["id"] = str(self.id)

        if self.alias is not None:
            base["alias"] = self.alias

        if self.credentials_id is not None:
            base["credentialsId"] = str(self.credentials_id)

        return base


###############################################################################
#                              Cloud Storage
###############################################################################


class S3Definition(StoreDefinition):
    type_str = StoreType.S3

    def __init__(self, bucket: str, key: str, file_format: FileFormat,
                 params: Optional[Dict[str, str]] = None, store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, S3Definition.type_str, store_id)
        self.bucket = bucket
        self.key = key
        self.file_format = file_format
        self.params = params

    def __repr__(self):
        return f'{self.__class__.__name__}(bucket: {self.bucket!r}, key: {self.key!r}, ' \
               f'file_format: {self.file_format!r}, params: {self.params})'

    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object with camelCase keys
        :return:
        """
        base = self._base_payload()
        base["bucket"] = self.bucket
        base["key"] = self.key
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _s3_definition_from_payload(d: dict) -> Union[DtlError, S3Definition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % (
            StoreDefinition.type_field))

    if type_field != S3Definition.type_str.value:
        return DtlError("The object %s is not an S3 definition" % (str(d)))

    bucket = d.get("bucket")
    if bucket is None:
        return DtlError("'bucket' needs to be defined in an S3 store")

    key = d.get("key")
    if key is None:
        return DtlError("'key' needs to be defined in an S3 store")

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in an S3 store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return S3Definition(bucket, key, file_format, params, store_id)


class GCSDefinition(StoreDefinition):
    type_str = StoreType.GCS

    def __init__(self, bucket: str, file_name: str, file_format: FileFormat,
                 params: Optional[Dict[str, str]] = None, store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, GCSDefinition.type_str, store_id)
        self.bucket = bucket
        self.file_name = file_name
        self.file_format = file_format
        self.params = params

    def __repr__(self):
        return f'{self.__class__.__name__}(bucket: {self.bucket!r}, file_name: {self.file_name!r}, ' \
               f'file_format: {self.file_format!r}, params: {self.params})'

    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object  with camelCase keys
        :return:
        """
        base = self._base_payload()
        base["bucket"] = self.bucket
        base["fileName"] = self.file_name
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _gcs_definition_from_payload(d: dict) -> Union[DtlError, GCSDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % (StoreDefinition.type_field))

    if type_field != GCSDefinition.type_str.value:
        return DtlError("The object %s is not a GCS definition" % (str(d)))

    bucket = d.get("bucket")
    if bucket is None:
        return DtlError("'bucket' needs to be defined in a GCS store")

    file_name = d.get("fileName")
    if file_name is None:
        return DtlError("'fileName' needs to be defined in a GCS store")

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in a GCS store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return GCSDefinition(bucket, file_name, file_format, params, store_id)


class AzureStorageDefinition(StoreDefinition):
    type_str = StoreType.AzureStorage

    def __init__(self, endpoint_protocol: str, blob_type: str,
                 container: str, file_name: str, file_format: FileFormat,
                 params: Optional[Dict[str, str]] = None, credentials_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, AzureStorageDefinition.type_str, credentials_id)
        self.endpoint_protocol = endpoint_protocol
        self.blob_type = blob_type
        self.container = container
        self.file_name = file_name
        self.file_format = file_format
        self.params = params

    def _as_payload(self) -> dict:
        """
        Dictionary representation of the object  with camelCase keys
        :return:
        """
        base = self._base_payload()
        base["endpointProtocol"] = self.endpoint_protocol
        base["blobType"] = self.blob_type
        base["container"] = self.container
        base["fileName"] = self.file_name
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _azure_storage_definition_from_payload(d: dict) \
        -> Union[DtlError, AzureStorageDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != AzureStorageDefinition.type_str.value:
        return DtlError("The object %s is not an Azure Storage definition" % (str(d)))

    endpoint_protocol = d.get("endpointProtocol")
    if endpoint_protocol is None:
        return DtlError("'endpointProtocol' needs to be defined in an Azure Storage store")

    blob_type = d.get("blobType")
    if blob_type is None:
        return DtlError("'blobType' needs to be defined in an Azure Storage store")

    container = d.get("container")
    if container is None:
        return DtlError("'container' needs to be defined in an Azure Storage store")

    file_name = d.get("fileName")
    if file_name is None:
        return DtlError("'fileName' needs to be defined in an Azure Storage store")

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in an Azure Storage store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return AzureStorageDefinition(endpoint_protocol, blob_type, container,
                                  file_name, file_format, params, store_id)


###############################################################################
#                              Database Connectors
###############################################################################

class JDBCDefinition(StoreDefinition):
    type_str = StoreType.JDBC

    def __init__(self, url: str, schema: str, user: str, password: str, root_table: str,
                 params: Optional[Dict[str, str]] = None, store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, JDBCDefinition.type_str, store_id)
        self.url = url
        self.schema = schema
        self.user = user
        self.password = password
        self.root_table = root_table
        self.params = params

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["url"] = self.url
        base["schema"] = self.schema
        base["user"] = self.user
        base["password"] = self.password
        base["rootTable"] = self.root_table
        if self.params is not None:
            base["params"] = self.params
        return base


def _jdbc_definition_from_payload(d: dict) -> Union[DtlError, JDBCDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != JDBCDefinition.type_str.value:
        return DtlError("The object %s is not a JDBC definition" % str(d))

    url = d.get("url")
    if url is None:
        return DtlError("'url' needs to be defined in a JDBC store")

    schema = d.get("schema")
    if schema is None:
        return DtlError("'schema' needs to be defined in a JDBC store")

    user = d.get("user")
    if user is None:
        return DtlError("'user' needs to be defined in a JDBC store")

    password = d.get("password")
    if password is None:
        return DtlError("'password' needs to be defined in a JDBC store")

    root_table = d.get("rootTable")
    if root_table is None:
        return DtlError("'rootTable' needs to be defined in a JDBC store")

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return JDBCDefinition(url, schema, user, password, root_table, params, store_id)


class MongoDefinition(StoreDefinition):
    type_str = StoreType.Mongo

    def __init__(self, url: str, database: str, user: str, password: str,
                 collection: str, params: Optional[Dict[str, str]] = None,
                 store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, MongoDefinition.type_str, store_id)
        self.url = url
        self.database = database
        self.user = user
        self.password = password
        self.collection = collection
        self.params = params
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["url"] = self.url
        base["database"] = self.database
        base["user"] = self.user
        base["password"] = self.password
        base["collection"] = self.collection
        if self.params is not None:
            base["params"] = self.params
        return base


def _mongo_definition_from_payload(d: dict) -> Union[DtlError, MongoDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != MongoDefinition.type_str.value:
        return DtlError("The object %s is not a Mongo definition" % str(d))

    url = d.get("url")
    if url is None:
        return DtlError("'url' needs to be defined in a Mongo store")

    database = d.get("database")
    if database is None:
        return DtlError("'database' needs to be defined in a Mongo store")

    user = d.get("user")
    if user is None:
        return DtlError("'user' needs to be defined in a Mongo store")

    password = d.get("password")
    if password is None:
        return DtlError("'password' needs to be defined in a Mongo store")

    collection = d.get("collection")
    if collection is None:
        return DtlError("'collection' needs to be defined in a Mongo store")

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return MongoDefinition(url, database, user, password, collection, params, store_id)


###############################################################################
#                              API Sources
###############################################################################


class SocrataDefinition(StoreDefinition):
    type_str = StoreType.Socrata

    def __init__(self, domain: str, token: str, socrata_id: str, params: Optional[Dict[str, str]] = None,
                 store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, SocrataDefinition.type_str, store_id)
        self.domain = domain
        self.token = token
        self.id = socrata_id
        self.params = params
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["domain"] = self.domain
        base["token"] = self.token
        base["id"] = self.id
        if self.params is not None:
            base["params"] = self.params
        return base


def _socrata_definition_from_payload(d: dict) -> Union[DtlError, SocrataDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != SocrataDefinition.type_str.value:
        return DtlError("The object %s is not a Socrata definition" % str(d))

    domain = d.get("domain")
    if domain is None:
        return DtlError("'domain' needs to be defined in a Socrata store")

    token = d.get("token")
    if token is None:
        return DtlError("'token' needs to be defined in a Socrata store")

    id = d.get("id")
    if id is None:
        return DtlError("'id' needs to be defined in a Socrata store")

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return SocrataDefinition(domain, token, id, params, store_id)


class HttpResourceDefinition(StoreDefinition):
    type_str = StoreType.HttpResource

    def __init__(self, url: str, file_format: FileFormat, params: Optional[Dict[str, str]] = None,
                 store_id: Optional[UUID] = None):
        StoreDefinition.__init__(self, HttpResourceDefinition.type_str, store_id)
        self.url = url
        self.file_format = file_format
        self.params = params
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["url"] = self.url
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _http_resource_definition_from_payload(
        d: dict) -> Union[DtlError, HttpResourceDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != HttpResourceDefinition.type_str.value:
        return DtlError("The object %s is not an HttpResource definition" % str(d))

    url = d.get("url")
    if url is None:
        return DtlError("'url' needs to be defined in an HttpResource store")

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in an HttpResource store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return HttpResourceDefinition(url, file_format, params, store_id)


###############################################################################
#                              File Sources
###############################################################################


class FileSystemDefinition(StoreDefinition):
    type_str = StoreType.FileSystem

    def __init__(self, location: str, file_format: FileFormat,
                 params: Optional[Dict[str, str]] = None,
                 store_id: Optional[UUID] = None):
        StoreDefinition.__init__(
            self, FileSystemDefinition.type_str, store_id)
        self.location = location
        self.file_format = file_format
        self.params = params
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["location"] = self.location
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _file_system_definition_from_payload(
        d: dict) -> Union[DtlError, FileSystemDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != FileSystemDefinition.type_str.value:
        return DtlError("The object %s is not a FileSystem definition" % str(d))

    location = d.get("location")
    if location is None:
        return DtlError("'location' needs to be defined in a FileSystem store")

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in a FileSystem store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return FileSystemDefinition(location, file_format, params, store_id)


class FileUploadDefinition(StoreDefinition):
    type_str = StoreType.FileUpload

    def __init__(self, file_format: FileFormat,
                 params: Optional[Dict[str, str]] = None,
                 store_id: Optional[UUID] = None):
        StoreDefinition.__init__(
            self, FileUploadDefinition.type_str, store_id)
        self.file_format = file_format
        self.params = params
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        base = self._base_payload()
        base["format"] = self.file_format.value
        if self.params is not None:
            base["params"] = self.params
        return base


def _file_upload_definition_from_payload(d: dict) -> Union[DtlError, FileUploadDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != FileUploadDefinition.type_str.value:
        return DtlError("The object %s is not a FileUpload definition" % str(d))

    file_format = d.get("format")
    if file_format is None:
        return DtlError("'file_format' needs to be defined in a FileUpload store")
    else:
        file_format = file_format_from_str(file_format)
        if isinstance(file_format, DtlError):
            return file_format

    params = d.get("params")
    store_id = d.get(StoreDefinition.id_field)

    return FileUploadDefinition(file_format, params, store_id)


###############################################################################
#                              The Infinite Abyss
###############################################################################

class VoidDefinition(StoreDefinition):
    type_str = StoreType.Void

    def __init__(self, store_id: Optional[UUID] = None):
        StoreDefinition.__init__(
            self, VoidDefinition.type_str, store_id)
        self.store_id = store_id

    def _as_payload(self) -> dict:
        """Dictionary representation of the object with camelCase keys"""
        return self._base_payload()


def _void_definition_from_payload(d: dict) -> Union[DtlError, VoidDefinition]:
    type_field = d.get(StoreDefinition.type_field)
    if not isinstance(type_field, str):
        return DtlError("string %s is missing from the json" % StoreDefinition.type_field)

    if type_field != VoidDefinition.type_str.value:
        return DtlError("The object %s is not a Void definition" % str(d))

    store_id = d.get(StoreDefinition.id_field)

    return VoidDefinition(store_id)


_data_definitions = dict([
    (S3Definition.type_str.value, _s3_definition_from_payload),
    (GCSDefinition.type_str.value, _gcs_definition_from_payload),
    (AzureStorageDefinition.type_str.value,
     _azure_storage_definition_from_payload),
    (JDBCDefinition.type_str.value, _jdbc_definition_from_payload),
    (MongoDefinition.type_str.value, _mongo_definition_from_payload),
    (HttpResourceDefinition.type_str.value,
     _http_resource_definition_from_payload),
    (SocrataDefinition.type_str.value, _socrata_definition_from_payload),
    (FileSystemDefinition.type_str.value,
     _file_system_definition_from_payload),
    (FileUploadDefinition.type_str.value,
     _file_upload_definition_from_payload),
    (VoidDefinition.type_str.value, _void_definition_from_payload),

])


def _store_definition_from_payload(json: dict) -> Union[DtlError, StoreDefinition]:
    type_field = json.get(StoreDefinition.type_field)
    if type_field is None:
        return DtlError("The store definition object doesn't have a '%s' property" % \
               StoreDefinition.type_field)

    parsing_function = _data_definitions.get(type_field)
    if parsing_function is None:
        return DtlError("Looks like '%s' datastore is not handled by the SDK" % \
               type_field)

    return parsing_function(json)


def _data_store_from_payload(json: dict) -> Union[DtlError, DataStore]:
    name = json.get("name")
    if name is None:
        return DtlError("'name' for a data store should be defined")

    definition = json.get("gate")
    if definition is None:
        return DtlError("'gate' for a data store should be defined'")
    else:
        definition = _store_definition_from_payload(definition)

    alias = json.get("alias")
    credentials_id = json.get("credentialsId")
    if credentials_id is not None:
        credentials_id = UUID(credentials_id)
    store_id = json.get("id")

    samples = json.get("samples")
    if samples is not None:
        samples = _parse_list(_parse_list(_cell_from_payload))(samples)
        if isinstance(samples, DtlError):
            return samples

    schema = json.get("schema")
    if schema is not None:
        schema = _parse_list(_parse_list(_cell_from_payload))(schema)
        if isinstance(schema, DtlError):
            return schema

    schema_paths = json.get("schemaPaths")
    if schema_paths is not None:
        schema_paths = _parse_list(_parse_string_list)(schema_paths)
        if isinstance(schema_paths, DtlError):
            return schema_paths

    return DataStore(name, definition, credentials_id, alias, store_id,
                     samples, schema, schema_paths)
