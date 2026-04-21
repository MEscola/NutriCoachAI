from app.services.tracking_service import classify_tracking

# Função para calcular a pontuação geral do usuário com base nos trackings
def calculate_score(trackings):
    if not trackings:
        return 0

    total = len(trackings)

    score = 0

    for t in trackings:
        status = classify_tracking(t.refeicoes, t.treino_realizado)

        if status == "completo":
            score += 1
        elif status == "parcial":
            score += 0.5

    return int((score / total) * 100)

from datetime import timedelta


# Função para calcular a sequência atual de dias completos do usuário
def calculate_streak(trackings):
    if not trackings:
        return 0

    trackings_sorted = sorted(trackings, key=lambda x: x.date, reverse=True)

    streak = 0
    last_date = None

    for t in trackings_sorted:
        status = classify_tracking(t.refeicoes, t.treino_realizado)

        if status != "completo":
            break

        if last_date:
            if t.date != last_date - timedelta(days=1):
                break

        streak += 1
        last_date = t.date

    return streak