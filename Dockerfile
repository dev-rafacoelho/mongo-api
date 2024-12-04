# Use uma imagem base do Python
FROM python:3.12-slim

# Setar o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema para pacotes Python que precisam de compilação
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    libuv1-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expôr a porta que o FastAPI vai rodar
EXPOSE 8000

# Rodar o comando do Uvicorn para iniciar o FastAPI
CMD ["uvicorn", "quickstart:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
