import os
from alembic import command
from alembic.config import Config


def run_migrations():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    alembic_path = os.path.join(base_dir, "alembic.ini")

    alembic_cfg = Config(alembic_path)

    command.upgrade(alembic_cfg, "head")