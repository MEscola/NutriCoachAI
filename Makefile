BACKEND_DIR := meu_app_fit
VENV=venv/bin
#não usar o activate pq ele serve para alterar o ambiente do terminal, e aqui queremos apenas usar os binários do venv
# cada linha do Makefile é executada em um shell separado, então o source não mantém o ambiente ativo para a próxima linha


.PHONY: dev seed dev-seed prod up down logs rebuild migrate revision shell clean 

# Desenvolvimento local (venv)
dev:
	cd $(BACKEND_DIR) && $(VENV)/uvicorn app.main:app --reload

seed:
	cd $(BACKEND_DIR) && $(VENV)/python -m app.seeds.seed 

# Rodar seed e depois iniciar o servidor de desenvolvimento
dev-seed: 
	$(MAKE) seed
	$(MAKE) dev

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

# Entrar no container (debug)
exec:
	docker exec -it nutricoach_api bash


# Rebuild completo (zera tudo)
rebuild:
	docker compose down -v
	docker compose up --build 

#MIGRATIONS

# rodar sempre em um banco que ja tem tabelas, mas quer atualizar o schema sem perder dados.
stamp:
	cd $(BACKEND_DIR) && $(VENV)/alembic stamp head

# Gerar nova migration (autogenerate)
revision:
	cd $(BACKEND_DIR) && $(VENV)/alembic revision --autogenerate -m "$(msg)"
	# Exemplo: make revision msg="Add new field to User model"

# Rodar migrações(salva dados)
upgrade:
	cd $(BACKEND_DIR) && $(VENV)/alembic upgrade head


# Limpar imagens e containers (cuidado!)
clean:
	docker system prune -f

#! Roda as migrations do zero (cuidado, apaga dados!)
reset-db:
	@echo "⚠️ Isso irá apagar todos os dados. Tem certeza? (y/n)"; \
	read ans; \
	if [ "$$ans" = "y" ]; then \
		cd $(BACKEND_DIR) && $(VENV)/alembic downgrade base && $(VENV)/alembic upgrade head; \
		echo "✅ Banco resetado"; \
	else \
		echo "❌ Cancelado"; \
	fi