import uuid

from sqlalchemy import select

from domain.entities.produto import Produto
from infrastructure.data.models.produto_model import ProdutoModel


class ProdutoRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(self, skip: int = 0, take: int = 100) -> list[Produto]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(ProdutoModel).offset(skip).limit(take)
            )
            return [
                Produto.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> Produto | None:
        async with self.session_factory() as session:
            result = await session.get(ProdutoModel, id)
            return (
                Produto.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Produto) -> Produto:
        async with self.session_factory() as session:
            model = ProdutoModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Produto.model_validate(model, from_attributes=True)

    async def update(self, entity: Produto) -> Produto | None:
        async with self.session_factory() as session:
            model = await session.get(ProdutoModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return Produto.model_validate(model, from_attributes=True)

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(ProdutoModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
