from sqlalchemy import Column, Float, String, DateTime, Boolean, Time, Integer
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
    nome = Column(String(255), nullable=True)
    idade = Column(Integer, nullable=True)
    peso = Column(Float, nullable=True)
    altura = Column(Float, nullable=True)
    sexo = Column(String(20), nullable=True)
    objetivo = Column(String(50), nullable=True)
    tipo_treino = Column(String(50), nullable=True)
    horario_treino = Column(Time, nullable=True) # Formato HH

    #controle
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    #Relacionamentos
    plans = relationship("Plan", back_populates="user")
    trackings = relationship("Tracking", back_populates="user")