from pymongo import MongoClient

def conectar_mongodb(username, token):
    uri = f"mongodb+srv://{username}:{token}@cluster0.sowongv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client["pockemon"]
    return db

