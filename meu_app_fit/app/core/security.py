from operator import sub

from fastapi import HTTPException ,status
import os
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from typing import Optional

from app.core.settings import Settings
from app.core.exceptions import UnauthorizedException
settings = Settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))

    payload = {
        "type": "access", # Adicionamos um campo "type" para diferenciar entre tokens de acesso e refresh
        "sub": subject, # "sub" é o campo padrão para o assunto do token, onde armazenamos o ID do usuário
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)

def create_refresh_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=int(settings.REFRESH_TOKEN_EXPIRE_DAYS))

    payload = {
        "type": "refresh", 
        "sub": subject,
        "exp": expire,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)


def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]) 

        user_id = payload.get("sub") # Pegamos o valor do campo "sub" do payload, que é onde armazenamos o ID do usuário
        
        if not user_id: # Se o campo "sub" não estiver presente no payload, significa que o token é inválido
            raise UnauthorizedException()
        
        return user_id
    except JWTError:
        raise UnauthorizedException()
            
    
    '''
    O campo "sub" é o campo padrão para o assunto do token, onde armazenamos o ID do usuário.
     usar a variavel sub ao inves de retornar o payload inteiro, para evitar expor informações desnecessárias do token.
     Assim, quando decodificamos o token, retornamos apenas o ID do usuário (sub) em vez de todo o payload, que pode conter outras informações sensíveis.
     Dessa forma, garantimos que apenas o necessário seja exposto e mantemos a segurança dos dados do token.
    '''

def decode_full_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise UnauthorizedException()


   