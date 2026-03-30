from pydantic import BaseModel
from typing import List

class Meal(BaseModel):
    id: int
    name: str
    description: str
    calories: int

class DailyPlan(BaseModel):
    user_id: int
    date: str  # Formato YYYY-MM-DD
    meals: List[Meal]