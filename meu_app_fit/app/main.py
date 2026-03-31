import os

from fastapi import FastAPI
from app.core.config import setup_cors
from meu_app_fit.app.database.migrations import run_migrations
from meu_app_fit.app.routes.ai_routes import router as coach_router

app = FastAPI()

setup_cors(app)

app.include_router(ai_routes.router)
app.include_router(tracking_routes.router)
app.include_router(dash_routes.router)

@app.get("/")
def home():
    return {"message": "API rodando 🚀"}

@app.on_event("startup")
def on_startup():
    if os.getenv("ENV") == "dev":
        run_migrations()