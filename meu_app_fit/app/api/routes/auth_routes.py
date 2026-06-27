from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import RefreshRequest, UserCreate, UserLogin, Token
from app.services.auth_service import register_user, login_user
from app.api.deps import get_db
from app.core.security import create_access_token, create_refresh_token, decode_full_token 
from app.api.deps import get_current_user
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

@router.get("/me", response_model=UserMeResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "nome": current_user.nome,
        "idade": current_user.idade,
        "peso": current_user.peso,
        "sexo": current_user.sexo,
        "objetivo": current_user.objetivo,
        "tipo_treino": current_user.tipo_treino,
    }


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
        
