import os
import random
from pymongo import MongoClient, GEOSPHERE

# Configuration MongoDB
host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", "27017"))
db_name = os.getenv("MONGO_DB", "test_db")
collection_name = os.getenv("MONGO_COLLECTION", "points")
username = os.getenv("MONGO_USERNAME", "admin")
password = os.getenv("MONGO_PASSWORD", "admin123")

# Connexion
mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/"
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Création d’un index géospatial
collection.create_index([("location", GEOSPHERE)])
print("✅ Created 2dsphere index on 'location' field.")

# Génération de points aléatoires
def generate_random_points(n):
    points = []
    for i in range(n):
        lat = round(random.uniform(-90.0, 90.0), 6)
        lon = round(random.uniform(-180.0, 180.0), 6)
        text = f"Random point #{i+1}"
        points.append({
            "location": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "description": text
        })
    return points

# Insertion
num_points = 10
documents = generate_random_points(num_points)
collection.insert_many(documents)

print(f"✅ Inserted {num_points} random geospatial points into MongoDB.")
