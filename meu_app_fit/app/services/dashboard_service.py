from uuid import UUID
from app.services.tracking_service import get_tracking


def calcular_aderencia(refeicoes: dict):
    total = len(refeicoes)
    feitas = sum(1 for r in refeicoes.values() if r)

    if total == 0:
        return 0

    return round((feitas / total) * 100, 2)


def gerar_mensagem(frequencia: float):
    if frequencia >= 80:
        return "Excelente!"
    elif frequencia >= 50:
        return "Bom, mas pode melhorar"
    return "Vamos melhorar amanhã"


def get_dashboard(user_id: UUID):
    tracking = get_tracking(user_id)

    if not tracking:
        return {"message": "Sem dados ainda"}

    frequencia = calcular_aderencia(tracking["refeicoes"])

    return {
        "frequencia": frequencia,
        "mensagem": gerar_mensagem(frequencia)
    }