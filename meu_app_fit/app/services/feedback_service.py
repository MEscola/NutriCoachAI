def generate_feedback(progress):
    aderencia = progress["aderencia"]
    media = progress["media_real"]
    meta = progress["meta"]

    if aderencia >= 90:
        return "Excelente consistência! Você está no caminho certo para evolução rápida."

    if aderencia >= 70:
        return f"Boa consistência ({media}/{meta}x por semana), mas dá pra melhorar."

    if aderencia >= 40:
        return f"Você está treinando em média {media}x/semana. Tente se aproximar de {meta}x."

    return "Baixa aderência. Comece com metas menores para ganhar consistência."