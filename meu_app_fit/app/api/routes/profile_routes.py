from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from meu_app_fit.app.api.deps import get_current_user
from meu_app_fit.app.db.session import get_db
from meu_app_fit.app.schemas.user import UserMeResponse, UserUpdate
from user import User


router = APIRouter(prefix="/profile", tags=["profile"])

@router.get(response_model=UserMeResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserMeResponse)
def update_me(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_profile(db, current_user, data)