from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator

from domain.exceptions.currency import CurrencyException


def validate_currency(v: Decimal) -> Decimal:
    if v < 0:
        raise CurrencyException(v)
    return v


CURRENCY = Annotated[Decimal, AfterValidator(validate_currency)]
