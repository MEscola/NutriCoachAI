from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.ia_schema import CoachRequest

from app.services.ai_service import (
    gerar_plano,
    gerar_resposta_duvida
)

from app.services.plan_service import (
    get_user_current_plan,
    save_ai_plan
)


router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)


@router.post("/plano")
def plano(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # 1. Procura o plano de hoje
    existing = get_user_current_plan(
        db,
        current_user.id
    )

    # 2. Se já existe, não chama a IA
    if existing:
        return {
            "tipo": "plano",
            "data": existing
        }

    # 3. Se não existe, chama a IA
    plan_data = gerar_plano(current_user)

    # 4. Salva o plano gerado
    plan = save_ai_plan(
        db,
        current_user.id,
        plan_data
    )

    # 5. Retorna o plano
    return {
        "tipo": "plano",
        "data": plan
    }


@router.post("/duvida")
def duvida(
    request: CoachRequest,
    current_user: User = Depends(get_current_user)
):

    resposta = gerar_resposta_duvida(
        current_user,
        request.mensagem
    )

    return {
        "tipo": "duvida",
        "data": resposta
    }