import uuid

from sqlalchemy import (
    CheckConstraint,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column

from domain.entities.abstractions.base import Base


class Estoque(Base):
    __tablename__ = "estoques"
    __table_args__ = (
        CheckConstraint("quantidade >= 0", name="chk_quantidade"),
        ForeignKeyConstraint(
            ["franquia_id", "franqueadora_id"],
            ["franquias.id", "franquias.franqueadora_id"],
            name="fk_franquia_franqueadora",
        ),
        ForeignKeyConstraint(
            ["produto_id", "franqueadora_id"],
            ["produtos.id", "produtos.franqueadora_id"],
            name="fk_produto_franqueadora",
        ),
        PrimaryKeyConstraint("franquia_id", "produto_id", name="pk_estoques"),
    )

    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    franquia_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    produto_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
