import os
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from typing import Optional

from app.core.settings import Settings
settings = Settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))

    payload = {
        "sub": subject, # "sub" é o campo padrão para o assunto do token, onde armazenamos o ID do usuário
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), os.getenv("ALGORITHM"))

def create_refresh_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")))

    payload = {
        "sub": subject,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(payload, os.getenv("SECRET_KEY"), os.getenv("ALGORITHM"))


def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        
        if "sub" not in payload:
            return None # "sub" é o campo onde armazenamos o ID do usuário, se não existir, o token é inválido
        
    except JWTError:
        return None