import datetime
import uuid
from decimal import Decimal
from typing import Optional

from domain.entities.abstractions.base import Base


class Funcionario(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    nome: str
    cargo_id: uuid.UUID
    salario: Decimal
    data_admissao: datetime.datetime
    status: str
    data_demissao: Optional[datetime.datetime] = None
