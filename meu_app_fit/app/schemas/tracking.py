from typing_extensions import Annotated
from uuid import UUID
from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


# ENUM
class RefeicaoStatusEnum(str, Enum): 
    done = "done"
    missed = "missed"


# CREATE
class RefeicaoStatusCreate(BaseModel):
    refeicao_id: int
    status: RefeicaoStatusEnum


class TrackingCreate(BaseModel):
    date: date
    refeicoes: Annotated[
        List[RefeicaoStatusCreate],
        Field(min_items=1, max_items=10)
    ]
    treino_realizado: bool  # Pode ser nulo se o usuário não tiver realizado nenhum treino


# RESPONSE
class RefeicaoStatusResponse(BaseModel):
    #id: int
    #user_id: UUID
    refeicao_id: int
    status: RefeicaoStatusEnum


class TrackingResponse(BaseModel):
    id: UUID
    user_id: UUID
    date: date
    refeicoes: List[RefeicaoStatusResponse]
    treino_realizado: bool  # Pode ser nulo se o usuário não tiver realizado nenhum treino

    class Config:
        from_attributes = True

class TrackingStatsResponse(BaseModel):
    total_dias: int
    dias_completos: int
    #dias_parciais: int
    dias_falhados: int
    aderencia_refeicoes: int
    aderencia_treino: int
    aderencia_geral: int

class TrackingTodayResponse(BaseModel):
    status: str
    tracking: Optional[TrackingResponse]

class TrackingInsightResponse(BaseModel):
    score: int
    streak: int
    aderencia_geral: int
    progresso_meta: int
    mensagem: Optional[str] = Field(default="", max_length=300)