import datetime
import uuid
from decimal import Decimal

from domain.entities.abstractions.base import Base


class LancamentoFinanceiro(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    tipo: str
    categoria_id: uuid.UUID
    valor: Decimal
    data_lancamento: datetime.datetime
    descricao: str
