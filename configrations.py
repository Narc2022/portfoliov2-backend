from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://eduCode:eduCodeAI243$$$@codeai.2ablb2s.mongodb.net/?appName=codeAi"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.codeaidb
collection = db["codeaidb_data"]
user_collection = db["users"]