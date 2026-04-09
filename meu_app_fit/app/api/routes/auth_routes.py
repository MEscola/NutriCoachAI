from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import UserCreate, UserLogin, Token
from app.services.auth_service import register_user, login_user
from app.api.deps import get_db
from app.core.security import create_access_token, create_refresh_token, decode_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
def register(data: UserCreate, db: Session = Depends(get_db)):
    token = register_user(db, data)

    if not token:
        # resposta genérica (anti-enumeração)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid request"
        )

    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, data)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return {"access_token": token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
def refresh(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = decode_token(refresh_token)

        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

        new_access_token = create_access_token(user_id)
        new_refresh_token = create_refresh_token(user_id)

        return {"access_token": new_access_token, 
                "refresh_token": new_refresh_token, 
                "token_type": "bearer"}
    
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")