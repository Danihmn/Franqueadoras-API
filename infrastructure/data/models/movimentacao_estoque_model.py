import datetime
import uuid

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
    Text,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.data.models.abstractions.base_model import BaseModel


class MovimentacaoEstoqueModel(BaseModel):
    __tablename__ = "movimentacoes_estoque"
    __table_args__ = (
        CheckConstraint("quantidade > 0", name="chk_quantidade"),
        CheckConstraint(
            "tipo::text = ANY (ARRAY['entrada'::character varying, 'saida'::character varying, 'ajuste'::character varying]::text[])",  # noqa: E501
            name="chk_tipo",
        ),
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
        PrimaryKeyConstraint("id", name="pk_movimentacoes_estoque"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    franquia_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    produto_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    tipo: Mapped[str] = mapped_column(String(10), nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    data_movimentacao: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
    motivo: Mapped[str] = mapped_column(Text, nullable=False)
