import uuid
from abc import ABC

from pydantic import BaseModel


class Base(ABC, BaseModel):
    id: uuid.UUID
