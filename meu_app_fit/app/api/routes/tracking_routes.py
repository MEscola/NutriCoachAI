from datetime import datetime, timezone

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.tracking import TrackingCreate, TrackingInsightResponse, TrackingResponse, TrackingStatsResponse, TrackingTodayResponse
from app.services.tracking_service import classify_tracking, get_tracking_stats, salvar_tracking
from app.api.deps import get_current_user
from app.models.user import User
from app.db.session import get_db
from app.models.tracking import Tracking
from app.models.goal import Goal
from app.services.goal_service import calculate_goal_progress
from app.services.insights_service import calculate_score, calculate_streak


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

# Endpoint para obter o tracking do dia atual
from datetime import datetime, timezone

@router.get("/today", response_model=TrackingTodayResponse)
def get_today_tracking(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    today = datetime.now(timezone.utc).date()

    tracking = db.query(Tracking).filter(
        Tracking.user_id == current_user.id,
        Tracking.date == today
    ).first()

    if not tracking:
        return TrackingTodayResponse(
            status="no_tracking",
            tracking=None
        )

    status = classify_tracking(
        tracking.refeicoes,
        tracking.treino_realizado
    )

    return TrackingTodayResponse(
        status=status,
        tracking=tracking,
    )

# Endpoint para obter as estatísticas de tracking do usuário
@router.get("/stats", response_model=TrackingStatsResponse)
def tracking_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_tracking_stats(db, current_user.id)

@router.get("/insights", response_model=TrackingInsightResponse)
def tracking_insights(
    currente_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    trackings = db.query(Tracking).filter(Tracking.user_id == currente_user.id).all()

    score = calculate_score(trackings)
    streak = calculate_streak(trackings)

    stats = get_tracking_stats(db, currente_user.id)

    goal = db.query(Goal).filter(
        Goal.user_id == currente_user.id).order_by(Goal.created_at.desc()).first()
    
    progresso_meta = 0

    if goal:
        progress = calculate_goal_progress(trackings, goal)
        progresso_meta = progress.get("progresso_total", 0)

    # 🔥 mensagem inteligente simples
    if score >= 80 and aderencia_geral >= 70:
        mensagem = "Excelente consistência!"

    elif score >= 60:
        mensagem = "Você está evoluindo, mas precisa de consistência."

    elif score >= 40:
        mensagem = "Progresso irregular. Tente manter frequência."

    else:
        mensagem = "Baixa consistência. Comece com metas menores."

    return {
        "score": score,
        "streak": streak,
        "aderencia_geral": stats["aderencia_geral"],
        "progresso_meta": progresso_meta,
        "mensagem": mensagem
    }
