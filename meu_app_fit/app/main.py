from fastapi import FastAPI

from app.core.cors import setup_cors
from app.core.settings import settings
from app.core.logging import setup_logging
from app.routes import auth_routes

from app.db.migrations import run_migrations

from app.routes import ai_routes, tracking_routes, dash_routes


app = FastAPI()

# Setup global
setup_logging()
setup_cors(app)

# Rotas
app.include_router(ai_routes.router)
app.include_router(tracking_routes.router)
app.include_router(dash_routes.router)
app.include_router(auth_routes.router)


@app.get("/")
def home():
    return {"message": "API rodando 🚀"}


@app.on_event("startup")
def on_startup():
    if settings.ENV == "dev":
        run_migrations()