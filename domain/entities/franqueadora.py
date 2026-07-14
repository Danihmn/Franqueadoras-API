import datetime

from domain.entities.abstractions.base import Base


class Franqueadora(Base):
    nome: str
    cnpj: str
    created_at: datetime.datetime
