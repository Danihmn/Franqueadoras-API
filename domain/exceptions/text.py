from domain.exceptions.domain import DomainException


class TextException(DomainException):
    def __init__(self, value):
        super().__init__(message=f"INVALID TEXT VALUE: {value!r}", code="INVALID_TEXT")
