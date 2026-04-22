#todo CRIAR ROTAS PARA DESAFIOS

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.challenge import Challenge
from app.models.challengeProgress import ChallengeProgress
#from app.api.dependencies import get_current_user
from app.schemas.challenge import ChallengeCreate, ChallengeProgressCreate, ChallengeResponse
from uuid import UUID   