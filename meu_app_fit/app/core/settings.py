from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Configurações do Pydantic
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    # Segurança
    SECRET_KEY: str = Field(..., description="Chave secreta da aplicação")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15  # curto (seguro)
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7     # longo (menos seguro, mas necessário para refresh)

    # Banco de dados
    DATABASE_URL: str = Field(..., description="URL de conexão com o banco")
    # Gemini IA
    GEMINI_API_KEY: str | None = None #opcional, pode ser carregada do .env, o alembic não precisa disso

    # Ambiente
    ENV: str = "dev"


# Instância global
settings = Settings()