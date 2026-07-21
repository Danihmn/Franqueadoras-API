import uuid

from sqlalchemy import select

from domain.entities.lancamento_financeiro import LancamentoFinanceiro
from infrastructure.data.models.lancamento_financeiro_model import (
    LancamentoFinanceiroModel,
)


class LancamentoFinanceiroRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(
        self, skip: int = 0, take: int = 100
    ) -> list[LancamentoFinanceiro]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(LancamentoFinanceiroModel).offset(skip).limit(take)
            )
            return [
                LancamentoFinanceiro.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> LancamentoFinanceiro | None:
        async with self.session_factory() as session:
            result = await session.get(LancamentoFinanceiroModel, id)
            return (
                LancamentoFinanceiro.model_validate(
                    result, from_attributes=True
                )
                if result
                else None
            )

    async def create(
        self, entity: LancamentoFinanceiro
    ) -> LancamentoFinanceiro:
        async with self.session_factory() as session:
            model = LancamentoFinanceiroModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return LancamentoFinanceiro.model_validate(
                model, from_attributes=True
            )

    async def update(
        self, entity: LancamentoFinanceiro
    ) -> LancamentoFinanceiro | None:
        async with self.session_factory() as session:
            model = await session.get(LancamentoFinanceiroModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return LancamentoFinanceiro.model_validate(
                model, from_attributes=True
            )

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(LancamentoFinanceiroModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
