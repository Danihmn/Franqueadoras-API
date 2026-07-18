import datetime
import uuid

from domain.entities.abstractions.base import Base
from domain.enums.status import Status
from domain.validators.text import NON_BLANK_STR


class Franquia(Base):
    franqueadora_id: uuid.UUID
    nome: NON_BLANK_STR
    endereco_id: uuid.UUID
    status: Status
    data_abertura: datetime.datetime
