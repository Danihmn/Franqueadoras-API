from domain.exceptions.domain import DomainException


class CNPJException(DomainException):
    def __init__(self, value):
        super().__init__(message=f"INVALID CNPJ: {value}", code="INVALID_CNPJ")
