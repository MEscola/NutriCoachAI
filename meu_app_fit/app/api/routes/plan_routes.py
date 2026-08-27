from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.plan import PlanCreate, PlanResponse
from app.api.deps import get_current_user
from app.models.user import User
from app.db.session import get_db

from app.services.plan_service import (
    get_user_current_plan,
    create_user_plan,
)


router = APIRouter(
    prefix="/plans",
    tags=["plans"]
)


@router.post(
    "/",
    response_model=PlanResponse,
    status_code=status.HTTP_201_CREATED
)
def create_plan_route(
    data: PlanCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_user_plan(
        db=db,
        user_id=current_user.id,
        data=data
    )


@router.get(
    "/current",
    response_model=PlanResponse
)
def current_plan(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    plan = get_user_current_plan(
        db=db,
        user_id=current_user.id
    )

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plano não encontrado"
        )

    return plan