import datetime
import uuid

from pydantic import model_validator

from domain.entities.abstractions.base import Base
from domain.enums.status import Status
from domain.exceptions.funcionario import FuncionarioException
from domain.validators.currency import CURRENCY
from domain.validators.text import NON_BLANK_STR


class Funcionario(Base):
    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    nome: NON_BLANK_STR
    cargo_id: uuid.UUID
    salario: CURRENCY
    data_admissao: datetime.datetime
    status: Status
    data_demissao: datetime.datetime | None = None

    @model_validator(mode="after")
    def check_data_demissao(self) -> "Funcionario":
        if (
            self.data_demissao is not None
            and self.data_demissao < self.data_admissao
        ):
            raise FuncionarioException(
                f"DATA_DEMISSAO {self.data_demissao} ANTERIOR A DATA_ADMISSAO {self.data_admissao}"  # noqa: E501
            )
        return self
