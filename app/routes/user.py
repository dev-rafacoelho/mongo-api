# routes/user.py
from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user import get_all_users , create_user , get_user_by_name


router = APIRouter()

@router.get("/usuarios")
async def get_users():
    users = get_all_users()
    return users

@router.post("/usuarios")
async def create_user_endpoint(user: UserCreate):
    new_user = create_user(user.model_dump())
    return {"message": "Usuário criado com sucesso!", "user": new_user}

@router.get("/usuarios/{nome}")
async def get_user_by_name_endpoint(nome: str):
    user = get_user_by_name(nome)
    if user:
        return user
    return {"message": "Usuário não encontrado"}
    