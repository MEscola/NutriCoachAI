import os
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings




def setup_cors(app):
    #ENV = os.getenv("ENV", "dev")

    origins = ["*"] if settings.ENV == "dev" else [
        "https://seu-app.vercel.app"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )