import datetime

from pydantic import field_validator

from domain.entities.abstractions.base import Base
from domain.value_objects.cnpj import CNPJ


class Franqueadora(Base):
    nome: str
    cnpj: CNPJ
    created_at: datetime.datetime

    @field_validator("cnpj", mode="before")
    @classmethod
    def validate_cnpj(cls, v):
        if isinstance(v, CNPJ):
            return v
        return CNPJ(v)
