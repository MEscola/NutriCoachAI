FROM python:3.11-slim

#Evitar que o Python escreva arquivos .pyc e que o buffer de saída seja desativado para que os logs sejam exibidos em tempo real
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instala dependências do sistema (psycopg2 precisa disso)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

#Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

 #Expor a porta 8000 para acessar a aplicação
EXPOSE 8000

#Iniciar a aplicação usando o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]