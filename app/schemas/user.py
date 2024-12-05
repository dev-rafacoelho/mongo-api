# app/schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    sobrenome: str
    telefone: str
    sexo: str
