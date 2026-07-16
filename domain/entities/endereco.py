from domain.entities.abstractions.base import Base


class Endereco(Base):
    cidade: str
    estado_sigla: str
    pais: str
    cep: str
