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

from core.data.models.abstractions.base_model import BaseModel


class CargoModel(BaseModel):
    __tablename__ = "cargos"
    __table_args__ = (
        ForeignKeyConstraint(
            ["franqueadora_id"], ["franqueadoras.id"], name="fk_franqueadora"
        ),
        PrimaryKeyConstraint("id", name="pk_cargos"),
        UniqueConstraint(
            "id", "franqueadora_id", name="uq_cargo_franqueadora"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    franqueadora_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    descricao: Mapped[str] = mapped_column(String(100), nullable=False)
