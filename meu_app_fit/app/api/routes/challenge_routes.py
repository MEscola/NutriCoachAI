from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.challenge import (
    ChallengeCreate,
    ChallengeResponse,
)

from app.schemas.progress import (
    ProgressCreate,
    ProgressResponse,
)

from app.services import challenge_service
from app.core.exceptions import BadRequestException, NotFoundException

router = APIRouter(prefix="/challenges", tags=["challenges"])


@router.post("/", response_model=ChallengeResponse)
def create_challenge(
    data: ChallengeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return challenge_service.create_challenge(db, current_user.id, data)
    except Exception as e:
        raise BadRequestException(str(e))

# Registrar progresso em desafio
@router.post("/{challenge_id}/progress", response_model=ProgressResponse)
def register_progress(
    challenge_id: UUID,
    data: ProgressCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return challenge_service.add_progress(
            db, challenge_id, current_user.id, data
        )
    except Exception as e:
        raise BadRequestException(str(e))


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

    progresses = challenge_service.get_challenge_progresses(db, challenge_id)
    return challenge_service.calculate_challenge_insight(challenge, progresses)


@router.get("/{challenge_id}/progresses", response_model=list[ProgressResponse])
def get_challenge_progresses(
    challenge_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    challenge = challenge_service.get_challenge_by_id(db, challenge_id, current_user.id)

    if not challenge:
        raise NotFoundException(message="Challenge not found")
    
    progress = challenge_service.get_challenge_progress(db, challenge_id)

    insight = challenge_service.calculate_challenge_insight(challenge, progress)

    return {
        "challenge": challenge,
        "progress": progress,
        "insight": insight
    }