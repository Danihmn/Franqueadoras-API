import uuid

from sqlalchemy import select

from domain.entities.funcionario import Funcionario
from infrastructure.data.models.funcionario_model import FuncionarioModel


class FuncionarioRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def get_all(
        self, skip: int = 0, take: int = 100
    ) -> list[Funcionario]:
        async with self.session_factory() as session:
            result = await session.scalars(
                select(FuncionarioModel).offset(skip).limit(take)
            )
            return [
                Funcionario.model_validate(m, from_attributes=True)
                for m in result.all()
            ]

    async def get_by_id(self, id: uuid.UUID) -> Funcionario | None:
        async with self.session_factory() as session:
            result = await session.get(FuncionarioModel, id)
            return (
                Funcionario.model_validate(result, from_attributes=True)
                if result
                else None
            )

    async def create(self, entity: Funcionario) -> Funcionario:
        async with self.session_factory() as session:
            model = FuncionarioModel(**entity.model_dump())
            session.add(model)
            await session.flush()
            return Funcionario.model_validate(model, from_attributes=True)

    async def update(self, entity: Funcionario) -> Funcionario | None:
        async with self.session_factory() as session:
            model = await session.get(FuncionarioModel, entity.id)
            if model is None:
                return None
            for field, value in entity.model_dump(exclude={"id"}).items():
                setattr(model, field, value)
            await session.flush()
            return Funcionario.model_validate(model, from_attributes=True)

    async def delete(self, id: uuid.UUID) -> bool:
        async with self.session_factory() as session:
            model = await session.get(FuncionarioModel, id)
            if model is None:
                return False
            await session.delete(model)
            return True
