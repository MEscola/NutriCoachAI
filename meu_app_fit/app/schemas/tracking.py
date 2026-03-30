from pydantic import BaseModel
from typing import List

class MealStatus(BaseModel):
    id: int
    user_id: int
    meal_id: int
    status: str  # Ex: "done", "missed"

class DailyTracking(BaseModel):
    user_id: int
    date: str  # Formato YYYY-MM-DD
    meals_status: List[MealStatus]