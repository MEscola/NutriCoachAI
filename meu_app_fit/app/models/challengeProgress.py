from sqlalchemy import Column, Date, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base import Base

class ChallengeProgress(Base):
    __tablename__ = "challenge_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    challenge_id = Column(UUID(as_uuid=True), ForeignKey("challenges.id"), nullable=False)

    date = Column(Date, nullable=False)

    realizado = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())