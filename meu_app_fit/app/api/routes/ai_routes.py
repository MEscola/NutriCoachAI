from fastapi import APIRouter
from app.schemas.user import DadosUsuario
from app.services.ai_service import gerar_plano, gerar_resposta_duvida

router = APIRouter()

@router.post("/plano")
def plano(dados: DadosUsuario):
    return gerar_plano(dados)


@router.post("/duvida")
def duvida(dados: DadosUsuario):
    return gerar_resposta_duvida(dados)