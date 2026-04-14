from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import get_db
from meu_app_fit.app.core.exceptions import DatabaseException

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/live")
def health_live():
    return {"status": "alive"}


# Endpoint para verificar a prontidão da aplicação, testando a conexão com o banco de dados
@router.get("/ready")
def health_ready(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1")) 
        return {"status": "ready"}
    except Exception:
        raise DatabaseException()
