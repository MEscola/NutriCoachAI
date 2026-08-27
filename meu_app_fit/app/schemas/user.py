from datetime import time
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class TipoRequest(str, Enum):
    PLANO = "plano"
    DUVIDA = "duvida"   

class Sexo(str, Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"

class TipoTreino(str, Enum):
    CROSSFIT = "crossfit"
    MUSCULACAO = "musculacao"
    CORRIDA = "corrida"

class Objetivo(str, Enum):
    HIPERTROFIA = "hipertrofia"
    EMAGRECIMENTO = "emagrecimento"
    PERFORMANCE = "performance"


#SCHEMA PARA DADOS DO USUÁRIO

class DadosUsuario(BaseModel):
    avatar_url: Optional[str] = Field(default=None)
    nome: str = Field(..., max_length=255)
    horario_treino: time # Formato HH:MM
    idade: int = Field(..., gt=0)
    peso: float = Field(..., gt=0)
    altura: Optional[float] = Field(default=None, gt=0)
    sexo: Sexo
    objetivo: Objetivo
    tipo_treino: TipoTreino
    mensagem: Optional[str] = Field(default=None, max_length=300)
    tipo: TipoRequest


#Entrada da requisição para atualizar os dados do usuário        
class UserUpdate(BaseModel):
    idade: int = Field(..., gt=0)
    peso: float = Field(..., gt=0)
    altura: float = Field(..., gt=0)
    sexo: Sexo
    objetivo: Objetivo
    tipo_treino: TipoTreino
    horario_treino: time


#resposta   
class UserMeResponse(BaseModel):
    id: UUID
    avatar_url: str | None = None
    nome: str | None = None
    idade: int | None = None
    peso: float | None = None
    altura: float | None = None
    sexo: str | None = None
    objetivo: str | None = None
    tipo_treino: str | None = None
    horario_treino: time | None = None

    class Config:
        from_attributes = True