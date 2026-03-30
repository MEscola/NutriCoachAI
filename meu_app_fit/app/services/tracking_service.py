from app.models.db_fake import TRACKING_DB


def salvar_tracking(data):
    TRACKING_DB.append(data)


def get_tracking(user_id):
    for t in reversed(TRACKING_DB):
        if t["user_id"] == user_id:
            return t
    return None