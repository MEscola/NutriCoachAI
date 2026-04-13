from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.tracking import TrackingCreate, TrackingResponse
from app.services.tracking_service import salvar_tracking
from app.api.deps import get_current_user
from app.models.user import User
from app.db.session import get_db
from app.models.tracking import Tracking

router = APIRouter(prefix="/tracking", tags=["tracking"])


@router.post("/", response_model=TrackingResponse, status_code=status.HTTP_201_CREATED)
def create_tracking(
    data: TrackingCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return salvar_tracking(db, current_user.id, data)



@router.get("/", response_model=list[TrackingResponse])
def list_tracking(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db.query(Tracking).filter(
        Tracking.user_id == current_user.id
    ).all()