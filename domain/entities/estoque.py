import uuid

from pydantic import BaseModel


class Estoque(BaseModel):
    """Não herda de Base pois a chave primária é composta, e não possui um campo 'id'"""

    franqueadora_id: uuid.UUID
    franquia_id: uuid.UUID
    produto_id: uuid.UUID
    quantidade: int
