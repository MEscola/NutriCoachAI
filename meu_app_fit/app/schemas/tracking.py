from pydantic import BaseModel
from typing import List

class RefeiçãoStatus(BaseModel):
    id: int
    user_id: int
    refeição_id: int
    status: str  # Ex: "done", "missed"

class MonitoramentoDiario(BaseModel):
    user_id: int
    date: str  # Formato YYYY-MM-DD
    refeicoes_status: List[RefeiçãoStatus]