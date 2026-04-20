from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.db.session import SessionLocal
from app.models.user import User
from app.models.goal import Goal
from app.models.tracking import Tracking
from app.core.security import hash_password


def run_seed_dev():
    db: Session = SessionLocal()

    try:
        print("DEV SEED START")

        # 1. USERS (idempotente)
        admin_email = "admin@nutricoach.ai"
        user_email = "user@nutricoach.ai"

        admin = db.query(User).filter(User.email == admin_email).first()
        if not admin:
            admin = User(
                email=admin_email,
                password=hash_password("admin123"),
            )
            db.add(admin)

        user = db.query(User).filter(User.email == user_email).first()
        if not user:
            user = User(
                email=user_email,
                password=hash_password("user123"),
            )
            db.add(user)

        db.commit()
        db.refresh(admin)
        db.refresh(user)

        print("Users ok")

        # 2. GOAL (1 por usuário)
        goal = db.query(Goal).filter(Goal.user_id == user.id).first()

        if not goal:
            goal = Goal(
                user_id=user.id,
                tipo="corrida",
                frequencia_semanal=3,
                duracao_semanas=4,
            )
            db.add(goal)
            db.commit()

        print("Goal ok")

        # 3. TRACKING (últimos 7 dias)
        today = date.today()

        for i in range(7):
            day = today - timedelta(days=i)

            existing = db.query(Tracking).filter(
                Tracking.user_id == user.id,
                Tracking.date == day
            ).first()

            if existing:
                continue

            tracking = Tracking(
                user_id=user.id,
                date=day,
                refeicoes=[
                    {"refeicao_id": 1, "status": "done"},
                    {"refeicao_id": 2, "status": "done"},
                ],
                treino_realizado=(i % 2 == 0),  # alterna treino
            )

            db.add(tracking)

        db.commit()

        print("Seed DEV finalizado")

    finally:
        db.close()