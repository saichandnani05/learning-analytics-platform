from pymongo import MongoClient

MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/learning_analytics"

def get_db():
    client = MongoClient(MONGO_URI)
    db = client.learning_analytics
    return db
