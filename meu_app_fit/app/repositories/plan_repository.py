from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.plan import Plan


def get_current_plan(
    db: Session,
    user_id: UUID
) -> Plan | None:

    return (
        db.query(Plan)
        .filter(Plan.user_id == user_id)
        .order_by(Plan.date.desc())
        .first()
    )


def get_plan_by_date(
    db: Session,
    user_id: UUID,
    plan_date: date
) -> Plan | None:

    return (
        db.query(Plan)
        .filter(
            Plan.user_id == user_id,
            Plan.date == plan_date
        )
        .first()
    )


def create_plan(
    db: Session,
    user_id: UUID,
    plan_date: date,
    alimentacao: dict,
    dica_extra: str | None = None
) -> Plan:

    plan = Plan(
        user_id=user_id,
        date=plan_date,
        alimentacao=alimentacao,
        dica_extra=dica_extra
    )

    db.add(plan)
    db.commit()
    db.refresh(plan)

    return plan