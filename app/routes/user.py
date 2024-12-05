from pymongo import MongoClient
from fastapi import HTTPException

# Conectar ao MongoDB
uri = "mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017"
client = MongoClient(uri)
db = client.get_database("teste")
collection = db.get_collection("teste")

async def get_all_users():
    try:
        all_users = collection.find({}, {"_id": 0})  # Não retorna o campo _id
        users = list(all_users)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao consultar usuários: " + str(e))
