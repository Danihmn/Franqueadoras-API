import uuid

from domain.entities.abstractions.base import Base
from domain.validators.text import NON_BLANK_STR


class LancamentoFinanceiroCategoria(Base):
    franqueadora_id: uuid.UUID
    descricao: NON_BLANK_STR
