from typing import Annotated

from pydantic import AfterValidator

from domain.exceptions.inventory import InventoryException


def validate_estoque_quantidade(v: int) -> int:
    if v < 0:
        raise InventoryException(
            value=v, message=f"QUANTIDADE EM ESTOQUE {v} NAO PODE SER NEGATIVA"
        )
    return v


ESTOQUE_QUANTITY = Annotated[int, AfterValidator(validate_estoque_quantidade)]
