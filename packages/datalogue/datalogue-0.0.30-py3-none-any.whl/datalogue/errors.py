from typing import Optional


def _enum_parse_error(enum_description: str, string: str) -> str:
    return "'%s' is not a valid %s" % (string, enum_description)


class DtlError(Exception):

    def __init__(self, message: str, cause: Optional['DtlError'] = None):
        # Call the base class constructor with the parameters it needs
        super(DtlError, self).__init__(message)
        self.message = message
        self.cause = cause

    def __eq__(self, other: 'DtlError'):
        if isinstance(self, other.__class__):
            return self.message == other.message
        return False
