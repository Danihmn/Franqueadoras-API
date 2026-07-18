import datetime
import uuid

from domain.entities.abstractions.base import Base
from domain.enums.movimentacao_estoque_tipo import MovimentacaoEstoqueTipo
from domain.validators.inventory_movement import QUANTITY
from domain.validators.text import NON_BLANK_STR


class MovimentacaoEstoque(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    produto_id: uuid.UUID
    tipo: MovimentacaoEstoqueTipo
    quantidade: QUANTITY
    data_movimentacao: datetime.datetime
    motivo: NON_BLANK_STR
