import datetime
import uuid
from typing import Optional

from domain.entities.abstractions.base import Base
from domain.enums.status import Status
from domain.validators.currency import CURRENCY


class Funcionario(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    nome: str
    cargo_id: uuid.UUID
    salario: CURRENCY
    data_admissao: datetime.datetime
    status: Status
    data_demissao: Optional[datetime.datetime] = None
