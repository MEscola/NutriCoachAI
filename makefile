.PHONY: dev prod up down logs rebuild migrate revision shell clean 

# Desenvolvimento local (venv)
dev:
	cd meu_app_fit && uvicorn main:app --reload

# Produção (Docker) foreground
prod:
	docker compose up --build

# Subir em background
up:
	docker compose up --build -d

# Parar containers
down:
	docker compose down

# Ver logs
logs:
	docker compose logs -f

# Rebuild completo (zera tudo)
rebuild:
	docker compose down -v
	docker compose up --build 

# Rodar migrations
migrate:
	cd meu_app_fit && alembic upgrade head

# Criar nova migration
revision:
	cd meu_app_fit && alembic revision --autogenerate -m "$(msg)"	# Exemplo: make revision msg="Add new field to User model"

# Entrar no container (debug)
shell:
	docker exec -it nutricoach_api bash

# Limpar imagens e containers (cuidado!)
clean:
	docker system prune -f