import uuid

from sqlalchemy import select

from domain.entities.lancamento_financeiro_categoria import (
    LancamentoFinanceiroCategoria,
)
from infrastructure.data.models.lancamento_financeiro_categoria_model import (
    LancamentoFinanceiroCategoriaModel,
)


class LancamentoFinanceiroCategoriaRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(
        self, skip: int = 0, take: int = 100
    ) -> list[LancamentoFinanceiroCategoria]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(LancamentoFinanceiroCategoriaModel)
                .offset(skip)
                .limit(take)
            )
            return [
                LancamentoFinanceiroCategoria.model_validate(
                    m, from_attributes=True
                )
                for m in result.all()
            ]

    async def get_by_id(
        self, id: uuid.UUID
    ) -> LancamentoFinanceiroCategoria | None:
        async with self.session_factory() as session:
            result = await session.get(
                LancamentoFinanceiroCategoriaModel, id
            )
            return (
                LancamentoFinanceiroCategoria.model_validate(
                    result, from_attributes=True
                )
                if result
                else None
            )

    async def create(
        self, entity: LancamentoFinanceiroCategoria
    ) -> LancamentoFinanceiroCategoria:
        async with self.session_factory() as session:
            model = LancamentoFinanceiroCategoriaModel(
                **entity.model_dump()
            )
            session.add(model)
            await session.flush()
            return LancamentoFinanceiroCategoria.model_validate(
                model, from_attributes=True
            )

    async def update(
        self, entity: LancamentoFinanceiroCategoria
    ) -> LancamentoFinanceiroCategoria | None:
        async with self.session_factory() as session:
            model = await session.get(
                LancamentoFinanceiroCategoriaModel, entity.id
            )
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return LancamentoFinanceiroCategoria.model_validate(
                model, from_attributes=True
            )

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(
                LancamentoFinanceiroCategoriaModel, id
            )
            if model is None:
                return False
            await session.delete(model)
            return True
