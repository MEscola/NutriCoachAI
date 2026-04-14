from datetime import date

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.tracking import TrackingCreate, TrackingResponse, TrackingStatsResponse, TrackingTodayResponse
from app.services.tracking_service import classify_tracking, get_tracking_stats, salvar_tracking
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

@router.get("/today", response_model=TrackingTodayResponse)
def get_today_tracking(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    today = date.today()

    tracking = db.query(Tracking).filter(
        Tracking.user_id == current_user.id,
        Tracking.date == today
    ).first()

    if not tracking:
       return {"status": "no_tracking", "tracking": None}
    
    status = classify_tracking(
        tracking.refeicoes, 
        tracking.treino_realizado
    )
    
    return {"status": status, "tracking": tracking}

@router.get("/stats", response_model=TrackingStatsResponse)
def tracking_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_tracking_stats(db, current_user.id)