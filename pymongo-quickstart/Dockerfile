# Use uma imagem base do Python
FROM python:3.10-slim

# Setar o diretório de trabalho
WORKDIR /app

# Copiar o código do projeto para o contêiner
COPY . /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expôr a porta que o FastAPI vai rodar
EXPOSE 8000

# Rodar o comando do Uvicorn para iniciar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
