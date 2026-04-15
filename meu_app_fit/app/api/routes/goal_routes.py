from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.goal import GoalProgressResponse, GoalResponse
from app.schemas.goal import GoalCreate
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.goal import Goal
from sqlalchemy.orm import Session

from app import db
from app.models.tracking import Tracking
from app.services.feedback_service import generate_feedback
from app.services.goal_service import calculate_goal_progress

router = APIRouter(prefix="/goals", tags=["goals"])

@router.post("/", response_model=GoalResponse)
def create_goal(
    data: GoalCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    goal = Goal(
        user_id=current_user.id,
        **data.dict()
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

# Rota para obter o progresso da meta
@router.get("/progress", response_model=GoalProgressResponse)
def goal_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    goal = db.query(Goal).filter(
        Goal.user_id == current_user.id
    ).order_by(Goal.start_date.desc()) .first()

    if not goal:
       return {
           "goal": None,
           "progress": {},
           "feedback": "Nenhuma meta definida"
    }

    inicio = goal.start_date

    trackings = db.query(Tracking).filter(
        Tracking.user_id == current_user.id,
        Tracking.date >= inicio
    ).all()

    if not trackings:
        return {
            "goal": goal,
            "progress": {
                "media_real": 0,
                "meta": goal.frequencia_semanal,
                "aderencia": 0,
                "progresso_total": 0
            },
            "feedback": "📌 Comece hoje! O primeiro treino já conta como progresso."
        }

    progress = calculate_goal_progress(trackings, goal)
    feedback = generate_feedback(progress)

    return {
        "goal": goal,
        "progress": progress,
        "feedback": feedback
    }