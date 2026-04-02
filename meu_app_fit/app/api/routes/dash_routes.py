from fastapi import APIRouter
from app.services.dashboard_service import get_dashboard

router = APIRouter()

@router.get("/dashboard/{user_id}")

def dashboard(user_id: str):
    return get_dashboard(user_id)