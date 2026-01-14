from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


for doc in collection.find({"code_insee" : "75120"}, {}).limit(10):
    print(doc["nom"])

for doc in collection.find({"hauteur" : {"$gt" : 20}}, {}).limit(10):
    print(doc["nom"])
    print("aaaaaaaaaaaaaaaaa")

for doc in collection.find(
    {"nom": {"$regex": "Chêne", "$options": "i"}},
    {"nom": 1, "_id": 0}):
    print(doc["nom"])

for doc in collection.find({"circonference" : {"$exists": True, "$gt": 3}}, {}):
    print(doc["nom"]," circonference : ",doc["circonference"])



for doc in collection.find({}, {}).sort("hauteur", 1).limit(10):
    print(doc["nom"]," hauteur : ",doc["hauteur"])



