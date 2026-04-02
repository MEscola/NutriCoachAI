from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Segurança
    SECRET_KEY: str = Field(..., description="Chave secreta da aplicação")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15  # curto (seguro)

    # Banco de dados
    DATABASE_URL: str = Field(..., description="URL de conexão com o banco")

    # Gemini IA
    GEMINI_API_KEY: str = Field(..., description="API Key do Gemini")

    # Ambiente
    ENV: str = "dev"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instância global
settings = Settings()