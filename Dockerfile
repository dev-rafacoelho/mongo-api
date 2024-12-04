# Use uma imagem base do Python
FROM python:3.10-slim

# Setar o diretório de trabalho
WORKDIR /app

# Copiar o código do projeto para o contêiner
COPY . /app

# Instalar dependências do sistema para pacotes Python que precisam de compilação
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    libuv1-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expôr a porta que o FastAPI vai rodar
EXPOSE 8000

# Rodar o comando do Uvicorn para iniciar o FastAPI
CMD ["uvicorn", "app.quickstart:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
