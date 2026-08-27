from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Alimentacao(BaseModel):
    pre_treino: str
    cafe: str
    pos_treino: str
    almoco: str
    jantar: str
    lanches: str


class PlanResponse(BaseModel):
    id: UUID
    user_id: UUID
    date: date
    alimentacao: Alimentacao
    dica_extra: str | None = None

    model_config = ConfigDict(from_attributes=True)


class PlanCreate(BaseModel):
    date: date
    alimentacao: Alimentacao
    dica_extra: str | None = None