from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserUpdate


def update_profile(
    db: Session,
    current_user: User,
    data: UserUpdate,
):
    current_user.idade = data.idade
    current_user.peso = data.peso
    current_user.sexo = data.sexo
    current_user.objetivo = data.objetivo
    current_user.tipo_treino = data.tipo_treino
    current_user.horario_treino = data.horario_treino

    db.commit()
    db.refresh(current_user)

    return current_user