import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

def setup_cors(app):
    ENV = os.getenv("ENV", "dev")

    origins = ["*"] if ENV == "dev" else [
        "https://seu-app.vercel.app"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["POST"],
        allow_headers=["*"],
    )