from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated, List

class Refeicao(BaseModel):
    id: int 

    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)

    calorias: int = Field(ge=0, le=5000)

class PlanCreate(BaseModel):
    date: date

    refeicoes: Annotated[
    List[Refeicao],
    Field(min_items=1, max_items=10)
]

class PlanResponse(BaseModel):
    id: UUID
    user_id: UUID
    date: date
    refeicoes: List[Refeicao]

    model_config = ConfigDict(from_attributes=True)