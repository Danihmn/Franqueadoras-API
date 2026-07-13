import uuid

from sqlalchemy import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from domain.entities.abstractions.base import Base


class LancamentoFinanceiroCategoria(Base):
    __tablename__ = "lancamentos_financeiros_categorias"
    __table_args__ = (
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        PrimaryKeyConstraint(
            "id", name="pk_lancamentos_financeiros_categorias"
        ),
        UniqueConstraint(
            "id", "franqueadora_id", name="uq_categoria_franqueadora"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    descricao: Mapped[str] = mapped_column(String(150), nullable=False)
