from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.manga import Manga
from models.chapter import Chapter
from schemas.schema import *
from bson import ObjectId
from config import *

man = APIRouter()


@man.get("/manga")
async def find_manga():
    return serialize_list(manga_collection.find())


@man.get("/manga/{manga_id}")
async def find_manga_by_id(manga_id):
    return serialize_dict(manga_collection.find_one({"_id": ObjectId(manga_id)}))


@man.post("/manga")
async def create_manga(manga: Manga):
    manga_collection.insert_one(jsonable_encoder(manga))
    return serialize_list(manga_collection.find())


@man.put("/manga/{manga_id}")
async def update_manga(manga_id, manga: Manga):
    manga_collection.find_one_and_update({"_id": ObjectId(manga_id)},
                                         {"$set": jsonable_encoder(manga)})
    return {"message": f"updated {manga_id} successfully"}


@app.put("/manga/{manga_id}/chapter")
async def update_manga_chapter(manga_id: str, chapter: Chapter):
    chapter_json = jsonable_encoder(chapter)
    manga_collection.find_one_and_update({"_id": ObjectId(manga_id)},
                                         {"$push": {"chapters": dict(chapter)}})
    return serialize_list(manga_collection.find())
