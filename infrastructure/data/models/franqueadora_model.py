import datetime
import uuid

from sqlalchemy import (
    DateTime,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.data.models.abstractions.base_model import BaseModel


class FranqueadoraModel(BaseModel):
    __tablename__ = "franqueadoras"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_franqueadoras"),
        UniqueConstraint("cnpj", name="uq_franqueadoras_cnpj"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(14), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
