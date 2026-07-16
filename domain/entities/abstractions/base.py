import uuid
from abc import ABC

from pydantic import BaseModel, Field


class Base(ABC, BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
