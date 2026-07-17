import uuid

from domain.entities.abstractions.base import Base
from domain.validators.currency import CURRENCY


class Produto(Base):
    franqueadora_id: uuid.UUID
    descricao: str
    preco_padrao: CURRENCY
    sku: str
