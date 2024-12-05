from fastapi import FastAPI
from app.routes.user import get_all_users  # Importando a função do arquivo users.py

app = FastAPI()

@app.get("/usuarios")
async def get_users():
    users = await get_all_users()  # Usando a função para obter os usuários
    return users
