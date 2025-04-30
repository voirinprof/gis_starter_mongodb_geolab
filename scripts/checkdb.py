import os
from pymongo import MongoClient

host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", "27017"))
db_name = os.getenv("MONGO_DB", "test_db")
collection_name = os.getenv("MONGO_COLLECTION", "test_collection")
username = os.getenv("MONGO_USERNAME", "admin")
password = os.getenv("MONGO_PASSWORD", "admin123")

# Construct the authenticated Mongo URI
mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/"
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

collection.insert_one({"message": "Hello from MongoDB with environment variables!"})
print("Inserted document:", collection.find_one())
