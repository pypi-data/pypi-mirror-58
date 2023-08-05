from datalogue.models.datastore import DatastoreDef
from datalogue.models.credentials import Credentials


class Source:
    def __init__(self, definition: DatastoreDef, credentials: Credentials):
        self.definition = definition
        self.credentials = credentials

    def _as_payload(self) -> dict:
        base = self.definition._as_payload().copy()
        base.update(self.credentials._as_payload())
        return base