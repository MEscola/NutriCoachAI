
from tokenize import String
from meu_app_fit.app.database.db import Base
from sqlalchemy import Column, String, Date, JSON
import uuid


class Plan(Base):
    __tablename__ = "plans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    refeicoes = Column(JSON, nullable=False)    
    dica_extra = Column(String, nullable=True)