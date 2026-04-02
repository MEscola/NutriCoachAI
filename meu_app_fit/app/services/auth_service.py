from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin
from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, data: UserCreate):
    existing_user = get_user_by_email(db, data.email)

    if existing_user:
        # NÃO revelar se já existe
        return None
    #raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já registrado") 
    #!Important - decidir se queremos revelar ou não a existência do email. Anti-enumeração é mais seguro, mas pode ser menos amigável.

    hashed = hash_password(data.password)

    user = create_user(db, data.email, hashed)

    token = create_access_token(str(user.id))

    return token


def login_user(db: Session, data: UserLogin):
    user = get_user_by_email(db, data.email)

    # mensagem genérica (anti-enumeração)
    if not user:
        return None

    if not verify_password(data.password, user.hashed_password):
        return None

    return create_access_token(str(user.id)) 
    #!Important - aqui também, a mensagem de erro é genérica para evitar enumeração. Decidir se queremos revelar ou não o motivo do erro.
    #return {"access_token": token, "token_type": "bearer"} - se quisermos seguir o padrão OAuth2, mas para simplicidade, podemos retornar só o token.