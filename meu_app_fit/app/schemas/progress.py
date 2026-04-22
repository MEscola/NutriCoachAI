from typing import Dict

from pydantic import BaseModel
from uuid import UUID
from datetime import date



class ProgressCreate(BaseModel):
    date: date
    realizado: int


class ProgressResponse(BaseModel):
    id: UUID
    date: date
    realizado: int

    class Config:
        from_attributes = True