# routes/user.py
from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user import get_all_users
from app.services.user import create_user

router = APIRouter()

@router.get("/usuarios")
async def get_users():
    users = get_all_users()
    return users

@router.post("/usuarios")
async def create_user_endpoint(user: UserCreate):
    # Convertendo o Pydantic model para um dicionário e processando
    new_user = create_user(user.dict())
    return {"message": "Usuário criado com sucesso!", "user": new_user}