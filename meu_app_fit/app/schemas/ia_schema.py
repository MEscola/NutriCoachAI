from pydantic import BaseModel


class CoachRequest(BaseModel):
    mensagem: str


class PlanoRequest(BaseModel):
    mensagem: str | None = None