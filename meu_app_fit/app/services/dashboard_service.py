from uuid import UUID
from sqlalchemy.orm import Session
from app.services.tracking_service import get_tracking_stats
from app.services.goal_service import calculate_goal_progress
from app.services.challenge_service import (
    get_current_challenge,
    get_challenge_progresses,
    calculate_challenge_insight
)
from app.models.tracking import Tracking
from app.models.goal import Goal


def calculate_user_score(db: Session, user_id: UUID):
    #TRACKING
    tracking_stats = get_tracking_stats(db, user_id)
    tracking_score = tracking_stats.get("aderencia_geral", 0)

    #GOAL
    goal = db.query(Goal).filter(
        Goal.user_id == user_id
    ).first()

    goal_score = 0
    goal_progress = 0

    if goal:
        trackings = db.query(Tracking).filter(
            Tracking.user_id == user_id
        ).all()

        progress = calculate_goal_progress(trackings, goal)

        goal_score = progress.get("aderencia", 0)
        goal_progress = progress.get("progresso_total", 0)

    #CHALLENGE
    challenge = get_current_challenge(db, user_id)

    challenge_score = 0
    challenge_progress = 0
    streak = 0
    challenge_message = None

    if challenge:
        progresses = get_challenge_progresses(db, challenge.id)
        insight = calculate_challenge_insight(challenge, progresses)

        challenge_score = insight.get("progresso", 0)
        challenge_progress = insight.get("progresso", 0)
        streak = insight.get("streak", 0)
        challenge_message = insight.get("mensagem")

    #SCORE FINAL
    score = int(
        (tracking_score * 0.4) +
        (goal_score * 0.3) +
        (challenge_score * 0.3)
    )

    #MENSAGENS
    if challenge_message:
        mensagem = challenge_message
    elif score >= 85:
        mensagem = "Excelente consistência! Continue assim."
    elif score >= 70:
        mensagem = "Bom progresso, você está evoluindo."
    elif score >= 50:
        mensagem = "Você pode melhorar sua consistência."
    else:
        mensagem = "Baixa aderência. Comece com pequenas metas."

    return {
        "score": score,
        "streak": streak,
        "aderencia_geral": tracking_score,
        "progresso_meta": goal_progress,
        "challenge_progresso": challenge_progress,
        "mensagem": mensagem,
    }

