from fastapi import FastAPI, APIRouter, HTTPException
from configrations import collection
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()
# auth

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