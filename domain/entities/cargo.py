import uuid

from domain.entities.abstractions.base import Base


class Cargo(Base):
    franqueadora_id: uuid.UUID
    descricao: str
