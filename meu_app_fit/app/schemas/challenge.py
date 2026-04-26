from enum import Enum
from typing import Dict, List

from pydantic import BaseModel
from uuid import UUID
from datetime import date

from app.schemas.progress import ProgressResponse


class UnidadeEnum(str, Enum):
    REPS = "reps"
    KM = "km"
    METROS = "metros"
    MINUTOS = "minutos"
    SEGUNDOS = "segundos"
    CALORIAS = "calorias"

class ChallengeCreate(BaseModel):
    tipo: str
    unidade: UnidadeEnum
    meta_total: int
    data_inicio: date
    data_fim: date


class ChallengeResponse(BaseModel):
    id: UUID
    tipo: str
    unidade: UnidadeEnum
    meta_total: int
    data_inicio: date
    data_fim: date

    class Config:
        from_attributes = True

class ChallengeInsightResponse(BaseModel):
    progresso: int
    streak: int
    atrasado: bool
    faltam_total: int
    precisa_por_dia: int
    mensagem: str

class ChallengeProgressFullResponse(BaseModel):
    challenge: ChallengeResponse
    progress: List[ProgressResponse]
    insight: ChallengeInsightResponse