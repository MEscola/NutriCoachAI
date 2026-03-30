from app.services.tracking_service import get_tracking


def calcular_aderencia(refeicoes):
    total = len(refeicoes)
    feitas = sum(1 for r in refeicoes.values() if r)

    if total == 0:
        return 0

    return round((feitas / total) * 100, 2)


def gerar_mensagem(aderencia):
    if aderencia >= 80:
        return "Excelente!"
    elif aderencia >= 50:
        return "Bom, mas pode melhorar"
    else:
        return "Vamos melhorar amanhã"


def get_dashboard(user_id):
    tracking = get_tracking(user_id)

    if not tracking:
        return {"message": "Sem dados ainda"}

    aderencia = calcular_aderencia(tracking["refeicoes"])

    return {
        "aderencia": aderencia,
        "mensagem": gerar_mensagem(aderencia)
    }