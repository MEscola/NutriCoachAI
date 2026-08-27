from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings


def setup_cors(app):

    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    if settings.ENV != "dev":
        origins.append("https://seu-app.vercel.app")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )