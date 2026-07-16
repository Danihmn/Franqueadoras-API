import datetime
import uuid
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKeyConstraint,
    Numeric,
    PrimaryKeyConstraint,
    String,
    Text,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.data.models.abstractions.base_model import BaseModel


class LancamentoFinanceiroModel(BaseModel):
    __tablename__ = "lancamentos_financeiros"
    __table_args__ = (
        CheckConstraint(
            "tipo::text = ANY (ARRAY['entrada'::character varying, 'saida'::character varying]::text[])",
            name="chk_tipo",
        ),
        CheckConstraint("valor > 0::numeric", name="chk_valor"),
        ForeignKeyConstraint(
            ["categoria_id", "franqueadora_id"],
            [
                "lancamentos_financeiros_categorias.id",
                "lancamentos_financeiros_categorias.franqueadora_id",
            ],
            name="fk_categoria_franqueadora",
        ),
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        ForeignKeyConstraint(
            ["franquia_id", "franqueadora_id"],
            ["franquias.id", "franquias.franqueadora_id"],
            name="fk_franquia_franqueadora",
        ),
        PrimaryKeyConstraint("id", name="pk_lancamentos_financeiros"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    tipo: Mapped[str] = mapped_column(String(10), nullable=False)
    categoria_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    valor: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    data_lancamento: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    franquia_id: Mapped[uuid.UUID] = mapped_column(Uuid)
