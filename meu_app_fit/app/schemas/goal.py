from typing import Dict

from pydantic import BaseModel
from uuid import UUID


class GoalCreate(BaseModel):
    tipo: str
    frequencia_semanal: int
    duracao_semanas: int


class GoalResponse(BaseModel):
    id: UUID
    tipo: str
    frequencia_semanal: int
    duracao_semanas: int

    class Config:
        from_attributes = True

class GoalProgressResponse(BaseModel):
    goal: GoalResponse
    progress: Dict
    feedback: str

    class Config:
        from_attributes = True