from sqlalchemy.orm import Session
from uuid import UUID

from app.models.tracking import Tracking
from app.schemas.tracking import TrackingCreate


def salvar_tracking(db: Session, user_id: UUID, data: TrackingCreate):
    #verificar se já existe (mesmo dia)
    refeicoes_dict = [r.model_dump() for r in data.refeicoes] # Converter os objetos RefeicaoCreate para dicionários
    
    existing = (
        db.query(Tracking)
        .filter(Tracking.user_id == user_id, Tracking.date == data.date)
        .first()
    )

    if existing:
        # update seguro
        existing.refeicoes = refeicoes_dict
        db.commit()
        db.refresh(existing)
        return existing

    tracking = Tracking(
        user_id=user_id,
        date=data.date,
        refeicoes=refeicoes_dict
    )

    db.add(tracking)
    db.commit()
    db.refresh(tracking)

    return tracking

#função para classificar o tracking
def classify_tracking(refeicoes, treino_realizado: bool) -> str:
    if not refeicoes:
        return "falhado"

    total = len(refeicoes)

    done_count = sum(
        1 for r in refeicoes if r["status"] == "done"
    )

    if done_count == total and treino_realizado:
        return "completo"

    if done_count == 0 and not treino_realizado:
        return "falhado"

    return "parcial"


# Função para calcular as estatísticas de tracking do usuário
def get_tracking_stats(db: Session, user_id: UUID):
    trackings = (
        db.query(Tracking)
        .filter(Tracking.user_id == user_id)
        .all()
    )

    total_dias = len(trackings)

    dias_completos = 0
    dias_refeicoes_ok = 0
    dias_treino_ok = 0

    for t in trackings:
        status = classify_tracking(t.refeicoes, t.treino_realizado)

    if status == "completo":
        dias_completos += 1

    if status != "falhado":
        dias_refeicoes_ok += 1  # ou refine depois

    if t.treino_realizado:
        dias_treino_ok += 1

    dias_falhados = total_dias - dias_completos

    def percent(valor):
        return int((valor / total_dias) * 100) if total_dias > 0 else 0

    return {
        "total_dias": total_dias,
        "dias_completos": dias_completos,
        "dias_falhados": dias_falhados,
        "aderencia_refeicoes": percent(dias_refeicoes_ok),
        "aderencia_treino": percent(dias_treino_ok),
        "aderencia_geral": percent(dias_completos),
    }