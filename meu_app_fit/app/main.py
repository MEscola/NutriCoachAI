from fastapi import FastAPI
from app.core.config import setup_cors
from app.routes.coach import router as coach_router

app = FastAPI()

setup_cors(app)

app.include_router(coach_router)

@app.get("/")
def home():
    return {"message": "API rodando 🚀"}