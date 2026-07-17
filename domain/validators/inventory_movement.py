from typing import Annotated

from pydantic import AfterValidator

from domain.exceptions.inventory import InventoryException


def validate_movement(v: int) -> int:
    if v <= 0:
        raise InventoryException(
            value=v, message=f"MOVEMENT {v} MUST BE GREATER THAN 0"
        )
    return v


QUANTITY = Annotated[int, AfterValidator(validate_movement)]
