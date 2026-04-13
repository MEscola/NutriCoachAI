from typing_extensions import Annotated
from uuid import UUID
from datetime import date
from enum import Enum
from typing import List

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

    class Config:
        from_attributes = True