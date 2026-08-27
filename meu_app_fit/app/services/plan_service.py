from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.plan import Plan
from app.repositories.plan_repository import (
    get_plan_by_date,
    create_plan,
)
from app.schemas.plan import PlanCreate


def get_user_current_plan(
    db: Session,
    user_id: UUID
) -> Plan | None:

    return get_plan_by_date(
        db=db,
        user_id=user_id,
        plan_date=date.today()
    )


def save_ai_plan(
    db: Session,
    user_id: UUID,
    plan_data: dict
) -> Plan:

    today = date.today()

    existing = get_plan_by_date(
        db=db,
        user_id=user_id,
        plan_date=today
    )

    if existing:
        return existing

    return create_plan(
        db=db,
        user_id=user_id,
        plan_date=today,
        alimentacao=plan_data["alimentacao"],
        dica_extra=plan_data.get("dica_extra")
    )


def create_user_plan(
    db: Session,
    user_id: UUID,
    data: PlanCreate
) -> Plan:

    existing = get_plan_by_date(
        db=db,
        user_id=user_id,
        plan_date=data.date
    )

    if existing:
        return existing

    return create_plan(
        db=db,
        user_id=user_id,
        plan_date=data.date,
        alimentacao=data.alimentacao.model_dump(),
        dica_extra=data.dica_extra
    )