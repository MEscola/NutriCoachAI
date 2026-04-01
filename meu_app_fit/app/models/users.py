
import uuid
from sqlalchemy import Column, String
from app.database.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    peso = Column(String, nullable=False)
    altura = Column(String, nullable=False)
    objetivo = Column(String, nullable=False)