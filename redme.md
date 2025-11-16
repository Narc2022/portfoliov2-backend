<!-- create our py envornment -->
python3 -m venv venv 

<!-- activated the environment -->
source venv/bin/activate or
venv\Scripts\activate

<!-- Library installed -->
pip install fastapi uvicon pymongo

✅ FastAPI + Uvicorn + PyMongo — What They Are Used For
1️⃣ FastAPI → Build APIs (backend application)

FastAPI is used to:

Create REST APIs (GET, POST, PUT, DELETE)

Handle authentication (JWT, OAuth)

Validate request/response models using Pydantic

Build scalable backend services

Auto-generate Swagger UI (/docs)

It is extremely fast and easy to write.


2️⃣ Uvicorn → Run the FastAPI server

Uvicorn is an ASGI web server used to:

Serve your FastAPI app

Handle async requests

Enable hot reload during development

Provide high performance

You run your app using:

uvicorn main:app --reload



3️⃣ PyMongo → Connect to MongoDB

PyMongo is used to:

Connect to MongoDB

Insert, update, delete, search documents

Manage collections

Perform queries, indexing, aggregation

Example usage:

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
users = db["users"]

users.insert_one({"name": "Sachin"})

<!--End libray installed -->

<!-- before connect mongo db we have to run in command -->
python -m pip install "pymongo[srv]" ## is not required in newer versions (like 4.15.4):

<!-- End before connect mongo db we have to run in command -->
