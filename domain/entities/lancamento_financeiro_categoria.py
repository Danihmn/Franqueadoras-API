import uuid

from domain.entities.abstractions.base import Base


class LancamentoFinanceiroCategoria(Base):
    franqueadora_id: uuid.UUID
    descricao: str
