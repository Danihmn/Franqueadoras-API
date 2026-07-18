import datetime

from domain.entities.abstractions.base import Base
from domain.validators.cnpj import CNPJ
from domain.validators.text import NON_BLANK_STR


class Franqueadora(Base):
    nome: NON_BLANK_STR
    cnpj: CNPJ
    created_at: datetime.datetime
