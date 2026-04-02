from fastapi import APIRouter, Depends, status

from app.schemas.plan import PlanCreate, PlanResponse
from app.services.plan_service import create_plan
from app.models.user import User
from app.api.deps import get_current_user


router = APIRouter(prefix="/plans", tags=["plans"])


@router.post("/", response_model=PlanResponse, status_code=status.HTTP_201_CREATED)
def create_plan(
    data: PlanCreate,
    current_user: User = Depends(get_current_user)
):
    return create_plan(current_user.id, data)