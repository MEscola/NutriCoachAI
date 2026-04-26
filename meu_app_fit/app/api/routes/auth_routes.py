from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import RefreshRequest, UserCreate, UserLogin, Token
from app.services.auth_service import register_user, login_user
from app.api.deps import get_db
from app.core.security import create_access_token, create_refresh_token, decode_full_token
from app.core.exceptions import UnauthorizedException
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
def register(data: UserCreate, db: Session = Depends(get_db)):
    token = register_user(db, data)

    return token


@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, data)

    return token

@router.post("/refresh", response_model=Token)
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):

    payload = decode_full_token(data.refresh_token)

    #valida tipo
    if payload.get("type") != "refresh":
        raise UnauthorizedException("Invalid token type")

    user_id = payload.get("sub")

    if not user_id:
        raise UnauthorizedException()

    user = db.query(User).filter(User.id == user_id).first()

    if not user or not user.is_active:
        raise UnauthorizedException()

    # gera novos tokens
    new_access_token = create_access_token(user_id)
    new_refresh_token = create_refresh_token(user_id)

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }
        
