from http.client import HTTPException

from sqlalchemy.orm import Session
from uuid import UUID

from app.models.plan import Plan
from app.schemas.plan import PlanCreate


def create_plan(db: Session, user_id: UUID, data: PlanCreate):
    existing = (
        db.query(Plan)
        .filter(Plan.user_id == user_id, Plan.date == data.date)
        .first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Plan already exists")

    plan = Plan(
        user_id=user_id,
        date=data.date,
        alimentacao=[r.dict() for r in data.refeicoes],
        dica_extra=None
    )

    db.add(plan)
    db.commit()
    db.refresh(plan)

    return plan