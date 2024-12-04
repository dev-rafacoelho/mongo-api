from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

# Conectar ao MongoDB
uri = "mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017"
client = MongoClient(uri)
db = client.get_database("teste")
collection = db.get_collection("teste")

app = FastAPI()

@app.get("/usuarios")
async def get_users():
    try:
        all_users = collection.find({}, {"_id": 0})  
        users = list(all_users)

        return users
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao consultar usuários: " + str(e))
