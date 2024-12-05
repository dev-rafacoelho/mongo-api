# services/user_service.py
from pymongo import MongoClient

def get_all_users():
    client = MongoClient("mongodb://mongo:rafael@easypanel.singularmodel.com.br:27017")
    db = client.get_database("teste")
    collection = db.get_collection("teste")
    
    users = collection.find({}, {"_id": 0})
    return list(users)
