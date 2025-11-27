from pydantic import BaseModel,EmailStr
from datetime import datetime

# auth models
class RegisterModel(BaseModel):
    username:str
    email:EmailStr
    mobile:str
    password: str

class LoginModel(BaseModel):
    username:str
    password:str

# user models
class Todo(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    is_deleted: bool = False
    updated_at: int = int(datetime.timestamp(datetime.now()))
    creation: int = int(datetime.timestamp(datetime.now()))