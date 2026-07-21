import uuid

from sqlalchemy import select

from domain.entities.endereco import Endereco
from infrastructure.data.models.endereco_model import EnderecoModel


class EnderecoRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(self, skip: int = 0, take: int = 100) -> list[Endereco]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(EnderecoModel).offset(skip).limit(take)
            )
            return [
                Endereco.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> Endereco | None:
        async with self.session_factory() as session:
            result = await session.get(EnderecoModel, id)
            return (
                Endereco.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Endereco) -> Endereco:
        async with self.session_factory() as session:
            model = EnderecoModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Endereco.model_validate(model, from_attributes=True)

    async def update(self, entity: Endereco) -> Endereco | None:
        async with self.session_factory() as session:
            model = await session.get(EnderecoModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return Endereco.model_validate(model, from_attributes=True)

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(EnderecoModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
