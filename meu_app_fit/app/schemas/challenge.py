from typing import Dict

from pydantic import BaseModel
from uuid import UUID
from datetime import date


class ChallengeCreate(BaseModel):
    tipo: str
    unidade: str
    meta_total: int
    data_inicio: date
    data_fim: date


class ChallengeResponse(BaseModel):
    id: UUID
    tipo: str
    unidade: str
    meta_total: int
    data_inicio: date
    data_fim: date

    class Config:
        from_attributes = True