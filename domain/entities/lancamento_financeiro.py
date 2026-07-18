import datetime
import uuid

from domain.entities.abstractions.base import Base
from domain.enums.lancamento_financeiro_tipo import LancamentoFinanceiroTipo
from domain.validators.currency import CURRENCY
from domain.validators.text import NON_BLANK_STR


class LancamentoFinanceiro(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    tipo: LancamentoFinanceiroTipo
    categoria_id: uuid.UUID
    valor: CURRENCY
    data_lancamento: datetime.datetime
    descricao: NON_BLANK_STR
