from fastapi import FastAPI

from app.core.cors import setup_cors
from app.core.settings import settings
#from app.core.logging import setup_logging
from app.api.routes import auth_routes

#from app.db.migrations import run_migrations

from app.api.routes import ai_routes, tracking_routes, dash_routes
from app.api.routes import health_routes
from app.api.routes import goal_routes
from app.api.routes import challenge_routes
from app.core.exception_handlers import app_exception_handler, generic_exception_handler
from app.core.middleware_log import LoggingMiddleware
from app.core.exceptions import AppException


app = FastAPI()

#middleware
app.add_middleware(LoggingMiddleware)

# Exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Setup global
setup_cors(app)

# Rotas
app.include_router(ai_routes.router)
app.include_router(tracking_routes.router)
app.include_router(dash_routes.router)
app.include_router(auth_routes.router)
app.include_router(health_routes.router)
app.include_router(goal_routes.router)
app.include_router(challenge_routes.router)


@app.get("/")
def home():
    return {"message": "API rodando 💪 "}


@app.on_event("startup")
def on_startup(): # Rodar migrações no startup
    #if settings.ENV == "dev":
        #run_migrations()
    pass    