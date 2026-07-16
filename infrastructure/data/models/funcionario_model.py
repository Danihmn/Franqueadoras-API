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
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.data.models.abstractions.base_model import BaseModel


class FuncionarioModel(BaseModel):
    __tablename__ = "funcionarios"
    __table_args__ = (
        CheckConstraint(
            "data_demissao IS NULL OR status::text = 'inativo'::text",
            name="chk_data_demissao",
        ),
        CheckConstraint("salario > 0::numeric", name="chk_salario"),
        CheckConstraint(
            "status::text = ANY (ARRAY['ativo'::character varying, 'inativo'::character varying]::text[])",  # noqa: E501
            name="chk_status",
        ),
        ForeignKeyConstraint(
            ["cargo_id", "franqueadora_id"],
            ["cargos.id", "cargos.franqueadora_id"],
            name="fk_cargo_franqueadora",
        ),
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        ForeignKeyConstraint(
            ["franquia_id"], ["franquias.id"], name="fk_franquia"
        ),
        PrimaryKeyConstraint("id", name="pk_funcionarios"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    franquia_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    cargo_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    salario: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    data_admissao: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
    status: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        server_default=text("'ativo'::character varying"),
    )
    data_demissao: Mapped[datetime.datetime] = mapped_column(DateTime(True))
