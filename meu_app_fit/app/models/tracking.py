# models/tracking.py

from sqlalchemy import Column, String, JSON
from app.database import Base
import uuid

class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    date = Column(String)
    refeicoes = Column(JSON)