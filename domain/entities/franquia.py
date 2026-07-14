import datetime
import uuid

from domain.entities.abstractions.base import Base


class Franquia(Base):
    franqueadora_id: uuid.UUID
    nome: str
    endereco_id: uuid.UUID
    status: str
    data_abertura: datetime.datetime
