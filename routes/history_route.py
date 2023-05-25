from fastapi import APIRouter, HTTPException
from models.user import User
from schemas.schema import *
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from config import *

his = APIRouter()


@his.get("/user/{user_id}")
async def get_history(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    d = []
    for h in user["history"]:
        chapter = chapter_collection.find_one({"_id": ObjectId(h)})
        manga = manga_collection.find_one({"_id": ObjectId(chapter["manga_id"])})
        author = author_collection.find_one({"_id": ObjectId(manga["author_id"])})
        d.append(
            {
                "manga": manga["name"],
                "author": author["name"],
                "chapter": chapter["title"]
            })
    print(d)
    return jsonable_encoder(d)
