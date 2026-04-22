from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.models.user import User
from app.db.session import get_db

from app.services.dashboard_service import calculate_user_score
from app.schemas.dashboard import DashboardScoreResponse


router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/", response_model=DashboardScoreResponse)
def dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return calculate_user_score(db, current_user.id)