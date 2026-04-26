from uuid import UUID
from datetime import date, timedelta
from sqlalchemy.orm import Session

from app.models.challenge import Challenge, ChallengeStatus
from app.models.challenge_progress import ChallengeProgress
from app.core.exceptions import BadRequestException, NotFoundException, NotFoundException


def create_challenge(db: Session, user_id: UUID, data):
    #impedir múltiplos desafios ativos
    existing = db.query(Challenge).filter(
        Challenge.user_id == user_id,
        Challenge.status == ChallengeStatus.ATIVO
    ).first()

    if existing:
        raise Exception("User already has an active challenge")
   

    challenge = Challenge(
        user_id=user_id,
        status=ChallengeStatus.ATIVO,
        **data.dict()
    )

    db.add(challenge)
    db.commit()
    db.refresh(challenge)

    return challenge


def add_progress(db: Session, challenge_id: UUID, user_id: UUID, data):
    challenge = db.query(Challenge).filter(
        Challenge.id == challenge_id,
        Challenge.user_id == user_id
    ).first()

    if not challenge:
        raise NotFoundException("Challenge not found")

    #validar período
    if data.date < challenge.data_inicio or data.date > challenge.data_fim:
        raise BadRequestException("Date outside challenge period")

    #evitar duplicidade
    existing = db.query(ChallengeProgress).filter(
        ChallengeProgress.challenge_id == challenge_id,
        ChallengeProgress.date == data.date
    ).first()

    if existing:
        raise BadRequestException("Progress for this date already exists")

    progress = ChallengeProgress(
        challenge_id=challenge_id,
        date=data.date,
        realizado=data.realizado
    )

    db.add(progress)
    db.commit()
    db.refresh(progress)

    return progress

# Buscar desafio ativo do usuário
def get_current_challenge(db: Session, user_id: UUID):

    return db.query(Challenge).filter(
        Challenge.user_id == user_id,
        Challenge.status == ChallengeStatus.ATIVO
    ).first()



# Gerar insights do desafio
def calculate_challenge_insight(challenge, progress):
    today = date.today()

    # total de dias do desafio
    total_days = (challenge.data_fim - challenge.data_inicio).days + 1

    #dias passados
    dias_passados = (today - challenge.data_inicio).days + 1
    dias_passados = max(0, min(dias_passados, total_days))

    #total realizado
    total_realizado = sum(p.realizado for p in progress)

    #progresso %
    progresso = int((total_realizado / challenge.meta_total) * 100) if challenge.meta_total > 0 else 0
    progresso = min(progresso, 100)

    #streak (dias seguidos com progresso)
    progress_sorted = sorted(progress, key=lambda x: x.date, reverse=True)

    streak = 0
    current_day = today

    for p in progress_sorted:
        if p.date == current_day and p.realizado > 0:
            streak += 1
            current_day = current_day - timedelta(days=1)
        else:
            break

    #quanto deveria ter feito até hoje
    esperado_ate_hoje = int((challenge.meta_total / total_days) * dias_passados)

    atrasado = total_realizado < esperado_ate_hoje

    faltam_total = max(0, challenge.meta_total - total_realizado)

    dias_restantes = max(1, (challenge.data_fim - today).days + 1)

    precisa_por_dia = int(faltam_total / dias_restantes)


    #mensagem inteligente
    if progresso == 100:
        mensagem = "Meta concluída! Excelente trabalho"

    elif atrasado:
        mensagem = f"Você está atrasado. Faça {precisa_por_dia} hoje para recuperar o ritmo."

    elif streak >= 3:
        mensagem = "Ótima consistência! Continue assim"

    else:
        mensagem = "Bom progresso, continue!"

    if challenge.status != ChallengeStatus.ATIVO:
        raise BadRequestException("Challenge is not active")

    return {
        "progresso": progresso,
        "streak": streak,
        "atrasado": atrasado,
        "faltam_total": faltam_total,
        "precisa_por_dia": precisa_por_dia,
        "mensagem": mensagem,
    }

# Buscar desafio por ID
def get_challenge_by_id(db, challenge_id, user_id):
    return db.query(Challenge).filter(
        Challenge.id == challenge_id,
        Challenge.user_id == user_id
    ).first()

# Buscar todos os progressos de um desafio
def get_challenge_progress(db: Session, challenge_id: UUID):
    return db.query(ChallengeProgress).filter(
        ChallengeProgress.challenge_id == challenge_id
    ).order_by(ChallengeProgress.date.asc()).all() 


def cancel_challenge(db: Session, challenge_id: UUID, user_id: UUID):
    challenge = db.query(Challenge).filter(
        Challenge.id == challenge_id,
        Challenge.user_id == user_id
    ).first()

    if not challenge:
        raise NotFoundException("Challenge not found")
    
    if challenge.status != ChallengeStatus.ATIVO:
        raise BadRequestException("Only active challenges can be canceled")

    challenge.status = ChallengeStatus.CANCELADO
    db.commit()
    db.refresh(challenge)

    return challenge
