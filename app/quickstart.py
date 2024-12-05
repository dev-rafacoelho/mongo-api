# main.py
from fastapi import FastAPI
from app.routes.user import router as user_router

app = FastAPI()

# Incluindo as rotas
app.include_router(user_router)
