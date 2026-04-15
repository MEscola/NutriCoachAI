def calculate_goal_progress(trackings, goal):
    total_days = len(trackings)

    dias_com_treino = sum(
        1 for t in trackings if t.treino_realizado
    )

    # semanas reais
    semanas = max(1, total_days / 7)

    media_semanal_real = dias_com_treino / semanas

    # proteção
    if goal.frequencia_semanal == 0:
        return {
            "media_real": 0,
            "meta": 0,
            "aderencia": 0
        }

    aderencia = int(
        (media_semanal_real / goal.frequencia_semanal) * 100
    )

    # limite
    aderencia = min(aderencia, 100)

    # NOVO — progresso total da meta
    total_meta = goal.frequencia_semanal * goal.duracao_semanas

    progresso_total = int(
        (dias_com_treino / total_meta) * 100
    ) if total_meta > 0 else 0

    return {
        "media_real": round(media_semanal_real, 2),
        "meta": goal.frequencia_semanal,
        "aderencia": aderencia,
        "progresso_total": min(progresso_total, 100)
    }