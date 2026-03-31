from pydantic import BaseModel
from typing import List

class Refeiçao(BaseModel):
    id: int
    name: str
    description: str
    calorias: int

class DailyPlan(BaseModel):
    user_id: int
    date: str  # Formato YYYY-MM-DD
    refeicoes: List[Refeiçao]