from fastapi import APIRouter
from app.schemas.user import DadosUsuario
from app.services.ai_service import gerar_plano, processar_requisicao

router = APIRouter()

@router.post("/perguntar")
async def responder_pergunta(dados: DadosUsuario):
    try:
        return processar_requisicao(dados)
    except Exception as e:
        return {
            "erro": "Falha ao gerar plano",
            "detalhe": str(e)
        }