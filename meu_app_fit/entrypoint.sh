#!/bin/sh

echo "🚀 Iniciando container..."

cd /app

if [ "$ENV" != "ci" ]; then
  echo "📦 Aplicando migrations..."
  alembic upgrade head || echo "⚠️ Falha na migration (não bloqueante)"
else
  echo "⚠️ CI: pulando migrations"
fi

echo "🌐 Subindo aplicação..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000