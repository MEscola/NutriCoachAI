from alembic import command
from alembic.config import Config

def run_migrations(): # Função para rodar as migrações
    alembic_cfg = Config("alembic.ini") # Certifique-se de que o caminho para o arquivo alembic.ini está correto
    command.upgrade(alembic_cfg, "head") # Atualiza o banco de dados para a última versão