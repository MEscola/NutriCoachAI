import os
from fastapi import Header, HTTPException

def verificar_token(x_token: str = Header(...)):
    if x_token != os.getenv("APP_TOKEN"):
        raise HTTPException(status_code=401, detail="Token inválido")
    
#todo código relacionado à autenticação e segurança pode ser colocado aqui, como funções para gerar tokens, verificar permissões, etc.