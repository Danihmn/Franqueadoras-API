import datetime
import uuid

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from domain.entities.abstractions.base import Base


class Franquia(Base):
    __tablename__ = "franquias"
    __table_args__ = (
        CheckConstraint(
            "status::text = ANY (ARRAY['ativo'::character varying, 'inativo'::character varying]::text[])",
            name="chk_status",
        ),
        ForeignKeyConstraint(
            ["endereco_id"], ["enderecos.id"], name="fk_endereco"
        ),
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        PrimaryKeyConstraint("id", name="pk_franquias"),
        UniqueConstraint(
            "id", "franqueadora_id", name="uq_franquia_franqueadora"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    endereco_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    status: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        server_default=text("'ativo'::character varying"),
    )
    data_abertura: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
