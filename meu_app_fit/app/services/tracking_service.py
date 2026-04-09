from sqlalchemy.orm import Session
from uuid import UUID

from app.models.tracking import Tracking
from app.schemas.tracking import TrackingCreate


def salvar_tracking(db: Session, user_id: UUID, data: TrackingCreate):
    #verificar se já existe (mesmo dia)
    existing = (
        db.query(Tracking)
        .filter(Tracking.user_id == user_id, Tracking.date == data.date)
        .first()
    )

    if existing:
        # update seguro
        existing.refeicoes = data.refeicoes
        db.commit()
        db.refresh(existing)
        return existing

    tracking = Tracking(
        user_id=user_id,
        date=data.date,
        refeicoes=data.refeicoes
    )

    db.add(tracking)
    db.commit()
    db.refresh(tracking)

    return tracking