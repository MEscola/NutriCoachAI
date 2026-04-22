from pydantic import BaseModel


class DashboardScoreResponse(BaseModel):
    score: int
    streak: int
    aderencia_geral: int
    progresso_meta: int
    challenge_progresso: int
    mensagem: str