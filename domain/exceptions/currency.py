from domain.exceptions.domain import DomainException


class CurrencyException(DomainException):
    def __init__(self, value):
        super().__init__(
            message=f"INVALID VALUE: {value}", code="INVALID_CURRENCY"
        )
