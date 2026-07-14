import uuid
from decimal import Decimal

from domain.entities.abstractions.base import Base


class Produto(Base):
    franqueadora_id: uuid.UUID
    descricao: str
    preco_padrao: Decimal
    sku: str
