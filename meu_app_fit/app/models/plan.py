from sqlalchemy import Column, String, Date, JSON
from app.database.db import Base
import uuid


class Plan(Base):
    __tablename__ = "plans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    alimentacao = Column(JSON, nullable=False)    
    dica_extra = Column(String, nullable=True)