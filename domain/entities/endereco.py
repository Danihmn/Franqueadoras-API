import uuid

from sqlalchemy import PrimaryKeyConstraint, String, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column

from domain.entities.abstractions.base import Base


class Endereco(Base):
    __tablename__ = "enderecos"
    __table_args__ = (PrimaryKeyConstraint("id", name="pk_enderecos"),)

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, server_default=text("gen_random_uuid()")
    )
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estado_sigla: Mapped[str] = mapped_column(String(2), nullable=False)
    pais: Mapped[str] = mapped_column(String(100), nullable=False)
    cep: Mapped[str] = mapped_column(String(8), nullable=False)
