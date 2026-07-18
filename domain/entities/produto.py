import uuid

from domain.entities.abstractions.base import Base
from domain.validators.currency import CURRENCY
from domain.validators.text import NON_BLANK_STR


class Produto(Base):
    franqueadora_id: uuid.UUID
    descricao: NON_BLANK_STR
    preco_padrao: CURRENCY
    sku: NON_BLANK_STR
