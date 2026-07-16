import datetime

from domain.entities.abstractions.base import Base
from domain.validators.cnpj import CNPJ


class Franqueadora(Base):
    nome: str
    cnpj: CNPJ
    created_at: datetime.datetime
