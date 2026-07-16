import datetime
import uuid

from domain.entities.abstractions.base import Base
from domain.enums.movimentacao_estoque_tipo import MovimentacaoEstoqueTipo


class MovimentacaoEstoque(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    produto_id: uuid.UUID
    tipo: MovimentacaoEstoqueTipo
    quantidade: int
    data_movimentacao: datetime.datetime
    motivo: str
