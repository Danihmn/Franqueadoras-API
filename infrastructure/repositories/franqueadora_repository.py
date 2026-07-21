import uuid

from sqlalchemy import select

from domain.entities.franqueadora import Franqueadora
from infrastructure.data.models.franqueadora_model import FranqueadoraModel


class FranqueadoraRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(
        self, skip: int = 0, take: int = 100
    ) -> list[Franqueadora]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(FranqueadoraModel).offset(skip).limit(take)
            )
            return [
                Franqueadora.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> Franqueadora | None:
        async with self.session_factory() as session:
            result = await session.get(FranqueadoraModel, id)
            return (
                Franqueadora.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Franqueadora) -> Franqueadora:
        async with self.session_factory() as session:
            model = FranqueadoraModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Franqueadora.model_validate(model, from_attributes=True)

    async def update(self, entity: Franqueadora) -> Franqueadora | None:
        async with self.session_factory() as session:
            model = await session.get(FranqueadoraModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return Franqueadora.model_validate(model, from_attributes=True)

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(FranqueadoraModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
