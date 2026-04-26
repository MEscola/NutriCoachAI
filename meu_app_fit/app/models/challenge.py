from app.db.base import Base
from sqlalchemy import Column, Date, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from enum import Enum
from sqlalchemy import Enum as SqlEnum


class ChallengeStatus(str, Enum):
    ATIVO = "ativo"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    tipo = Column(String, nullable=False)  # flexoes, corrida, etc
    unidade = Column(String, nullable=False)

    meta_total = Column(Integer, nullable=False)

    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    status = Column(SqlEnum(ChallengeStatus), default=ChallengeStatus.ATIVO)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    