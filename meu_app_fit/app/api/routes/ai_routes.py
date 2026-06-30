from fastapi import APIRouter, Depends
from httpx import request
from app.schemas.user import DadosUsuario
from app.services.ai_service import gerar_plano, gerar_resposta_duvida
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/plano")
def plano(
    current_user: User = Depends(get_current_user)
):
    return gerar_plano(current_user)


@router.post("/duvida")
def duvida(
    current_user: User = Depends(get_current_user)
):
    return gerar_resposta_duvida(current_user, request.mensagem)