from uuid import UUID

from proto import Enum, Field
from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import List

class RefeicaoStatusEnum(str, Enum): 
    done = "done"
    missed = "missed"

class RefeicaoStatus(BaseModel):
    id: int
    user_id: UUID
    refeicao_id: int
    status: RefeicaoStatusEnum

class MonitoramentoDiario(BaseModel):
    user_id: UUID
    date: date  
    refeicoes_status: List[RefeicaoStatus] = Field(
        min_length=1,
        max_length=10 
    )