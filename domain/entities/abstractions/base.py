import uuid
from abc import ABC
from typing import Annotated

from pydantic import BaseModel, Field


class Base(ABC, BaseModel):
    id: Annotated[uuid.UUID, Field(default_factory=uuid.uuid4)]
