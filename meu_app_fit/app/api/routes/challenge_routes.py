from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.challenge import (
    ChallengeCreate,
    ChallengeInsightResponse,
    ChallengeProgressFullResponse,
    ChallengeResponse,
)

from app.schemas.progress import (
    ProgressCreate,
    ProgressResponse,
)

from app.services import challenge_service


router = APIRouter(prefix="/challenges", tags=["challenges"])


@router.post("/", response_model=ChallengeResponse)
def create_challenge(
    data: ChallengeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
        return challenge_service.create_challenge(db, current_user.id, data)

# Registrar progresso em desafio
@router.post("/{challenge_id}/progress", response_model=ProgressResponse)
def register_progress(
    challenge_id: UUID,
    data: ProgressCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
  
    return challenge_service.add_progress(
            db, challenge_id, current_user.id, data
        )
   


@router.get("/current", response_model=ChallengeResponse | None)
def get_current_challenge(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return challenge_service.get_current_challenge(db, current_user.id)


@router.get("/{challenge_id}/insight")
def get_challenge_insight(
    challenge_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    challenge = challenge_service.get_challenge_by_id(db, challenge_id, current_user.id)

    progress = challenge_service.get_challenge_progress(db, challenge_id)

    return challenge_service.calculate_challenge_insight(challenge, progress)


@router.get("/{challenge_id}/progress", response_model=ChallengeProgressFullResponse)
def get_challenge_progress(
    challenge_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    challenge = challenge_service.get_challenge_by_id(db, challenge_id, current_user.id)

    progress = challenge_service.get_challenge_progress(db, challenge_id)

    insight = challenge_service.calculate_challenge_insight(challenge, progress)

    return {
        "challenge": challenge,
        "progress": progress,
        "insight": insight
    }

@router.patch("/{challenge_id}/cancel", response_model=ChallengeResponse) #router.patch para indicar que é uma atualização parcial
def cancel_challenge(
    challenge_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
        return challenge_service.cancel_challenge(db, challenge_id, current_user.id)
    