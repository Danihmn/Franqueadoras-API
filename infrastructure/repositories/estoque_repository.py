import uuid

from sqlalchemy import select

from domain.entities.estoque import Estoque
from infrastructure.data.models.estoque_model import EstoqueModel


class EstoqueRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(self, skip: int = 0, take: int = 100) -> list[Estoque]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(EstoqueModel).offset(skip).limit(take)
            )
            return [
                Estoque.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(
        self, franquia_id: uuid.UUID, produto_id: uuid.UUID
    ) -> Estoque | None:
        async with self.session_factory() as session:
            result = await session.get(
                EstoqueModel, (franquia_id, produto_id)
            )
            return (
                Estoque.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Estoque) -> Estoque:
        async with self.session_factory() as session:
            model = EstoqueModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Estoque.model_validate(model, from_attributes=True)

    async def update(self, entity: Estoque) -> Estoque | None:
        async with self.session_factory() as session:
            model = await session.get(
                EstoqueModel, (entity.franquia_id, entity.produto_id)
            )
            if model is None:
                return None
            for field, value in entity.model_dump(
                exclude={"franquia_id", "produto_id"}
            ).items():
                setattr(model, field, value)
            await session.flush()
            return Estoque.model_validate(model, from_attributes=True)

    async def delete(
        self, franquia_id: uuid.UUID, produto_id: uuid.UUID
    ) -> bool:
        async with self.session_factory() as session:
            model = await session.get(
                EstoqueModel, (franquia_id, produto_id)
            )
            if model is None:
                return False
            await session.delete(model)
            return True
