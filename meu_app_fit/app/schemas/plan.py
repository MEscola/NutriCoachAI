from datetime import date
from click import UUID
from pydantic import BaseModel, Field
from typing import List

class Refeicao(BaseModel):
    id: int 

    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)

    calorias: int = Field(ge=0, le=5000)

class PlanCreate(BaseModel):
    date: date

    refeicoes: List[Refeicao] = Field(
        min_length=1,
        max_length=10
    )

class PlanResponse(BaseModel):
    id: UUID
    user_id: UUID
    date: date
    refeicoes: List[Refeicao]

    class Config:
        from_attributes = True