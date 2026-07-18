from domain.exceptions.domain import DomainException


class EnderecoException(DomainException):
    def __init__(self, message: str):
        super().__init__(message=message, code="INVALID_ENDERECO")
