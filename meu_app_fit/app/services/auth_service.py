from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin
from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import create_refresh_token, hash_password, verify_password, create_access_token


def register_user(db: Session, data: UserCreate):
    existing_user = get_user_by_email(db, data.email)

    if existing_user:
        # NÃO revelar se já existe
        #return None    #!Important - decidir se queremos revelar ou não a existência do email. Anti-enumeração é mais seguro, mas pode ser menos amigável.
       
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid credentials"  # mensagem genérica para evitar enumeração
        )

    hashed = hash_password(data.password)
    user = create_user(db, data.email, hashed)
    token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"USER CRIADO: {user.email} and id: {user.id}") #!DEBUG

    return {"access_token": token, "refresh_token": refresh_token, "token_type": "bearer"}

   

    # mensagem genérica (anti-enumeração)
def login_user(db: Session, data: UserLogin):

    user = get_user_by_email(db, data.email)

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))
    
    return {"access_token": token, "refresh_token": refresh_token, "token_type": "bearer"}

 
    # seguir o padrão OAuth2, mas para simplicidade, podemos retornar só o token.