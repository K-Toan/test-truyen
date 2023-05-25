from fastapi import APIRouter, HTTPException
from models.user import User
from schemas.schema import *
from bson import ObjectId
from config import *

usr = APIRouter()


@usr.post("/register")
async def create_user(user: User):
    user_collection.insert_one(dict(user))
    return serialize_list(user_collection.find())


@usr.put("/user/{user_id}")
async def change_password(user_id: str, new_password: str):
    user_collection.find_one_and_update({"_id": ObjectId(user_id)},
                                        {"$set": {"password": new_password}})
    return {"message": f"updated pwd for {user_id} successfully"}


@usr.put("/user/{user_id}/chapter/{chapter_id}")
async def read(user_id: str, chapter_id: str):
    chapter = chapter_collection.find_one({"_id": ObjectId(chapter_id)})
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    user_collection.find_one_and_update({"_id": ObjectId(user_id)},
                                        {"$push": {"history": chapter_id}})

    return serialize_dict(user_collection.find_one({"_id": ObjectId(user_id)}))
