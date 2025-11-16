from fastapi import FastAPI, APIRouter
from configrations import collection
from database.schemas import all_tasks

app = FastAPI()
router = APIRouter()

@router.get("/v1/api")
async def get_all_todos():
    data = collection.find()
    return all_tasks(data)


app.include_router(router)