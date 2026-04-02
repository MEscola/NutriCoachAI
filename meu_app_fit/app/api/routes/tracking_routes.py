from fastapi import APIRouter
from app.services.tracking_service import salvar_tracking

router = APIRouter()

@router.post("/tracking")
def tracking(data: dict):
    
    salvar_tracking(data)
    return {"message": "Tracking salvo com sucesso"}