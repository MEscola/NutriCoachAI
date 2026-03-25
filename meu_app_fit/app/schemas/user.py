from pydantic import BaseModel, Field
from typing import Optional

#SCHEMA PARA DADOS DO USUÁRIO

class DadosUsuario(BaseModel):
    horario_treino: str = Field(..., pattern=r"^\d{2}:\d{2}$") # Formato HH:MM
    idade: int = Field(..., gt=0)
    peso: float = Field(..., gt=0)
    sexo: str = Field(..., min_length=1)
    objetivo: str = Field(..., min_length=1)
    tipo_treino: str = Field(..., min_length=1)
    mensagem: Optional[str] = ""
    tipo: str = Field(..., pattern="^(plano|duvida)$")