from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.dashboard_service import get_dashboard
from app.api.deps import get_current_user
from app.models.user import User
from app.db.session import get_db


router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/")
def dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_dashboard(db, current_user.id)