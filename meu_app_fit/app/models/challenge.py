from app.db.base import Base
from sqlalchemy import Column, Date, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid


class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    tipo = Column(String, nullable=False)  # flexoes, corrida, etc
    unidade = Column(String, nullable=False)  # reps, km, min

    meta_total = Column(Integer, nullable=False)

    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())