import uuid

from sqlalchemy import select

from domain.entities.movimentacao_estoque import MovimentacaoEstoque
from infrastructure.data.models.movimentacao_estoque_model import (
    MovimentacaoEstoqueModel,
)


class MovimentacaoEstoqueRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(
        self, skip: int = 0, take: int = 100
    ) -> list[MovimentacaoEstoque]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(MovimentacaoEstoqueModel).offset(skip).limit(take)
            )
            return [
                MovimentacaoEstoque.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> MovimentacaoEstoque | None:
        async with self.session_factory() as session:
            result = await session.get(MovimentacaoEstoqueModel, id)
            return (
                MovimentacaoEstoque.model_validate(
                    result, from_attributes=True
                )
                if result
                else None
            )

    async def create(
        self, entity: MovimentacaoEstoque
    ) -> MovimentacaoEstoque:
        async with self.session_factory() as session:
            model = MovimentacaoEstoqueModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return MovimentacaoEstoque.model_validate(
                model, from_attributes=True
            )

    async def update(
        self, entity: MovimentacaoEstoque
    ) -> MovimentacaoEstoque | None:
        async with self.session_factory() as session:
            model = await session.get(MovimentacaoEstoqueModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return MovimentacaoEstoque.model_validate(
                model, from_attributes=True
            )

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(MovimentacaoEstoqueModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
