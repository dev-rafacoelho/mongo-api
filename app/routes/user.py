# routes/user.py
from fastapi import APIRouter
from app.services.user import get_all_users

router = APIRouter()

@router.get("/usuarios")
async def get_users():
    users = get_all_users()
    return users
