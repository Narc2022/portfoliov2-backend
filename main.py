from fastapi import FastAPI, APIRouter, HTTPException, BackgroundTasks
from configrations import collection,user_collection
from database.schemas import all_tasks
from database.models import Todo,RegisterModel,LoginModel,ForgotPasswordRequest,ResetPasswordRequest
from utils.auth import hash_password, verify_password,create_access_token,verify_reset_token,create_reset_token
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()

# auth
# ----------------- Register API -----------------
@router.post("/register")
def register_user(data: RegisterModel):
    if user_collection.find_one({"username":data.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pwd = hash_password(data.password)
    
    user_data = {
        "username": data.username,
        "email":data.email,
        "mobile":data.mobile,
        "password":hashed_pwd
    }
    
    user_collection.insert_one(user_data)
    return {"message" : "User registered successfully"}

# ------------------ Login API ------------------
@router.post("/login")
def login_user(data:LoginModel):
    user = user_collection.find_one({"username":data.username})
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token({"username": data.username})
    
    return {
        "message" : "Login successful",
        "access_token" : token
    }
    

# @router.post("/forgot-password")
# async def forgot_password(request: ForgotPasswordRequest, background_tasks: BackgroundTasks):
#     # Check if user exists in DB
#     user = fake_users_db.get(request.email)  # replace with DB query
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     reset_token = create_reset_token(request.email)

#     # Send reset email in background
#     reset_link = f"http://localhost:3000/reset-password?token={reset_token}"
#     background_tasks.add_task(send_reset_email, request.email, reset_link)

#     return {"message": "Password reset link sent"}

# @router.post("/reset-password")
# async def reset_password(request: ResetPasswordRequest):
#     email = verify_reset_token(request.token)

#     if not email:
#         raise HTTPException(status_code=400, detail="Invalid or expired token")

#     # Fetch user by email
#     user = fake_users_db.get(email)  # replace with DB query
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Update password
#     user["password"] = hash_password(request.new_password)
    
#     return {"message": "Password updated successfully"}


# todos
@router.get("/todos")
async def get_all_todos():
    data = collection.find()
    return all_tasks(data)

@router.post("/todos")
async def create_task(new_task:Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.put("/todos/{task_id}")
async def update_task(task_id:str,updated_task:Todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code=404,detail=f"Task does not exist")
        updated_task.updated_at = datetime.now()
        resp = collection.update_one({"id":id},{"$set":dict(updated_task)})
        return{"status_code":200, "message":"Task updated successfully"}
    
    except Exception as e:
        return HTTPException(status_code=500,detail=f"Some error occured {e}")
            
app.include_router(router)