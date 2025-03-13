from pymongo import MongoClient
import json
from src.config import TEST_JSON_DB

client = MongoClient("mongodb://localhost:27017/")

db = client["card_pool"]
collection = db["cards"]

json_path = TEST_JSON_DB
print(json_path)

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)

if isinstance(data, list):
    print("liste")
    collection.insert_many(data)
    print("données insérées")
else:
    print("non")
