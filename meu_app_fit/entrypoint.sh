#!/bin/sh

echo "Iniciando container..."

echo "Aplicando migrations..."
alembic upgrade head || {
  echo "❌ Erro ao rodar migrations"
  exit 1
}

if [ "$ENV" = "dev" ]; then
  echo "DEV: rodando seed"
  python -m app.seeds.run_seed
fi

echo "Subindo aplicação..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000