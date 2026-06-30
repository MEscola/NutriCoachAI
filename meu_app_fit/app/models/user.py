from sqlalchemy import Column, Float, String, DateTime, Boolean, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    #login
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    #dados do usuário
    avatar_url = Column(String(255), nullable=True)
    nome = Column(String(255), nullable=False)
    idade = Column(String(3), nullable=False)
    peso = Column(Float(10), nullable=False)
    altura = Column(Float(10), nullable=True)
    sexo = Column(String(20), nullable=False)
    objetivo = Column(String(50), nullable=False)
    tipo_treino = Column(String(50), nullable=False)
    horario_treino = Column(Time, nullable=False)  # Formato HH

    #controle
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    #Relacionamentos
    plans = relationship("Plan", back_populates="user")
    trackings = relationship("Tracking", back_populates="user")