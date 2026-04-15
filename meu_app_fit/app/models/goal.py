from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    tipo = Column(String, nullable=False)  # Ex: corrida, crossfit, musculação, etc.

    start_date = Column(DateTime(timezone=True), server_default=func.now())  # Data de início da meta

    frequencia_semanal = Column(Integer, nullable=False)  # Quantas vezes por semana o usuário pretende treinar
    duracao_semanas = Column(Integer, nullable=False)  # Por quantas semanas o usuário pretende seguir esse plano

    created_at = Column(DateTime(timezone=True), server_default=func.now())