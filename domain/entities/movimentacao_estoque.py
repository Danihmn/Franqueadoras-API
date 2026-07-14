import datetime
import uuid

from domain.entities.abstractions.base import Base


class MovimentacaoEstoque(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    produto_id: uuid.UUID
    tipo: str
    quantidade: int
    data_movimentacao: datetime.datetime
    motivo: str
