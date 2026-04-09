from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.models.user import User
from app.db.session import get_db
from app.core.exceptions import UnauthorizedException
security = HTTPBearer()


def get_current_user( 
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials

    user_id = decode_token(token)

    if not user_id:
        raise UnauthorizedException()

    user = db.query(User).filter(User.id == user_id).first()

    if not user or not user.is_active:
        raise UnauthorizedException()

    return user

"""
deps.py

Centraliza dependências reutilizáveis da aplicação.

Exemplos:
- get_current_user → autenticação - 
    dependência que vamos usar para proteger rotas, garantindo que só usuários autenticados possam acessá-las.

- get_db → sessão do banco
- outras dependências compartilhadas entre rotas
"""