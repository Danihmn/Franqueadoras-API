from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from core.settings import settings

engine = create_async_engine(settings.database_url)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


@asynccontextmanager
async def get_session():
    session = async_session()

    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
