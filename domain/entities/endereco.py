from domain.entities.abstractions.base import Base
from domain.validators.endereco import CEP, UF
from domain.validators.text import NON_BLANK_STR


class Endereco(Base):
    cidade: NON_BLANK_STR
    estado_sigla: UF
    pais: NON_BLANK_STR
    cep: CEP
