# services/user_service.py
from pymongo import MongoClient

def get_all_users():
    client = MongoClient("mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017")
    db = client.get_database("teste")
    collection = db.get_collection("teste")
    
    users = collection.find({}, {"_id": 0})
    return list(users)  

def create_user(user_data: dict) -> dict:
    client = MongoClient("mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017")
    new_user = user_data
    db = client.get_database("teste")
    collection = db.get_collection("teste")

    result = collection.insert_one(user_data)
    new_user = collection.find_one({"_id": result.inserted_id}, {"_id": 0})  # Busca o usuário criado sem o campo `_id`
    return new_user

def get_user_by_name(nome: str) -> dict:
    client = MongoClient("mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017")
    db = client.get_database("teste")
    collection = db.get_collection("teste")
    
    user = collection.find_one({"nome": nome}, {"_id": 0})  # Busca pelo nome e retorna sem o campo "_id"
    return user