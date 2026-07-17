from domain.exceptions.domain import DomainException


class InventoryException(DomainException):
    def __init__(self, value, message: str | None = None):
        super().__init__(
            message=message
            if message is not None
            else f"INVALID INVENTORY MOVEMENT VALUE: {value}",
            code="INVALID_INVENTORY_MOVEMENT",
        )
