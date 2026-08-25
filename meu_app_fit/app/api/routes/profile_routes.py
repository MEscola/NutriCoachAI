from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.deps import get_current_user
from app.schemas.user import UserMeResponse, UserUpdate
from app.models.user import User
from app.services.profile_service import update_profile


router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/me", response_model=UserMeResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserMeResponse)
def update_me(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_profile(db, current_user, data)