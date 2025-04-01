from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://younes:3oM7fELiYA2Wa7QB@recruitpro.dsmqp.mongodb.net/?retryWrites=true&w=majority&appName=RecruitPro"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["masante_db"]  

collection = db["patients"] 

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")

    test_document = {
        "name": "John Doe",
        "age": 30,
        "medical_condition": "Healthy",
    }
    insert_result = collection.insert_one(test_document)
    print(f"✅ Inserted document ID: {insert_result.inserted_id}")

    retrieved_doc = collection.find_one({"_id": insert_result.inserted_id})
    print("✅ Retrieved document:", retrieved_doc)

except Exception as e:
    print(f"❌ Connection failed: {e}")
