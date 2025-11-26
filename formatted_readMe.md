Here is your **fully formatted README.md** — clean, professional, and ready to paste into GitHub.

---

# 🚀 FastAPI + MongoDB Authentication Setup

This guide explains how to set up a FastAPI project with MongoDB, including environment creation, library installation, and initial project structure.

---

## ✅ Step 1: Create Python Virtual Environment

```bash
python3 -m venv venv
```

---

## ✅ Step 2: Activate the Environment

### 🔹 On Linux / macOS:

```bash
source venv/bin/activate
```

### 🔹 On Windows:

```bash
venv\Scripts\activate
```

---

## ✅ Step 3: Install Required Libraries

```bash
pip install fastapi uvicorn pymongo
```

---

## 📦 What These Libraries Are Used For

### **1️⃣ FastAPI → Build Backend APIs**

FastAPI helps you:

* Create REST APIs (GET, POST, PUT, DELETE)
* Implement authentication (JWT, OAuth)
* Validate input/output using Pydantic
* Generate automatic API docs at `/docs`
* Build fast and scalable backend apps

---

### **2️⃣ Uvicorn → Run the FastAPI Server**

Uvicorn is an ASGI server and is used to:

* Run your FastAPI app
* Handle asynchronous requests
* Provide high performance
* Enable auto-reload

Start server:

```bash
uvicorn main:app --reload
```

---

### **3️⃣ PyMongo → Connect to MongoDB**

PyMongo allows you to:

* Connect to MongoDB
* Insert, update, delete documents
* Query collections
* Perform aggregation

Example:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
users = db["users"]

users.insert_one({"name": "Sachin"})
```

---

## ✅ Step 4: (Optional) Install SRV support for MongoDB Atlas

For MongoDB Atlas connections:

```bash
python -m pip install "pymongo[srv]"
```

> Note: This is **not required** in newer PyMongo versions (4.15.4+).

---

## ✅ Step 5: Create Configuration File

Create a file (e.g., `config.py` or `db.py`) to store MongoDB connection logic.

---

## ✅ Step 6: Create `database/` Folder

Inside this folder, you will place:

* Database connection
* Models
* Schemas
* CRUD helper functions

---

## ✅ Step 7: Create `models.py`

In FastAPI, **models** usually refer to Pydantic models which help with:

* Request validation
* Response formatting
* Auto-documentation
* Data serialization

Example:

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
```

---

## ✅ Step 8: Create `schemas.py`

This file contains schema definitions for:

* Request bodies
* Response models
* Data transformation

---

## ✅ Step 9: Create Utility Functions Inside Schemas

You may create two helper functions to:

* Format MongoDB data
* Convert ObjectId to string

Now everything is ready to start writing your APIs.

---

# 🎉 Setup Complete — You Can Now Write Login & Register APIs

If you want, I can also provide:

✔ Full FastAPI + MongoDB Authentication System
✔ JWT Access Tokens
✔ Password Hashing
✔ Protected Routes
✔ Complete Folder Structure

Just tell me:
**“generate full auth project”** or **“create login and register API”**.
