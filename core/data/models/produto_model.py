import uuid
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    ForeignKeyConstraint,
    Numeric,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from core.data.models.abstractions.base_model import BaseModel


class ProdutoModel(BaseModel):
    __tablename__ = "produtos"
    __table_args__ = (
        CheckConstraint("preco_padrao > 0::numeric", name="chk_preco_padrao"),
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        PrimaryKeyConstraint("id", name="pk_produtos"),
        UniqueConstraint("franqueadora_id", "sku", name="uq_sku"),
        UniqueConstraint(
            "id", "franqueadora_id", name="uq_produto_franqueadora"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    descricao: Mapped[str] = mapped_column(String(250), nullable=False)
    preco_padrao: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False
    )
    sku: Mapped[str] = mapped_column(String(50), nullable=False)
