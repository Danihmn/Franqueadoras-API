import uuid

from sqlalchemy import select

from domain.entities.franquia import Franquia
from infrastructure.data.models.franquia_model import FranquiaModel


class FranquiaRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(self, skip: int = 0, take: int = 100) -> list[Franquia]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(FranquiaModel).offset(skip).limit(take)
            )
            return [
                Franquia.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> Franquia | None:
        async with self.session_factory() as session:
            result = await session.get(FranquiaModel, id)
            return (
                Franquia.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Franquia) -> Franquia:
        async with self.session_factory() as session:
            model = FranquiaModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Franquia.model_validate(model, from_attributes=True)

    async def update(self, entity: Franquia) -> Franquia | None:
        async with self.session_factory() as session:
            model = await session.get(FranquiaModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return Franquia.model_validate(model, from_attributes=True)

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(FranquiaModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
