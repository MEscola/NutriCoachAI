# models/tracking.py

from sqlalchemy import Column, Date, ForeignKey, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.db.base import Base


class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    date = Column(Date, nullable=False)

    refeicoes = Column(JSONB, nullable=False)  # Armazena as refeições do dia em formato JSON   
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False) # Armazena a data e hora de criação do registro
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
    Index("idx_tracking_user_date", "user_id", "date", unique=True), # Garante que cada usuário tenha apenas um registro de tracking por dia
)

    user = relationship("User", back_populates="trackings")