from fastapi import APIRouter, HTTPException
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


@man.get("/manga/{manga_id}", response_model=Manga)
async def find_manga_by_id(manga_id: str):
    manga = manga_collection.find_one({"_id": ObjectId(manga_id)})
    if manga:
        return manga
    raise HTTPException(status_code=404, detail="Manga not found")


@man.post("/manga")
async def create_manga(manga: Manga):
    manga_collection.insert_one(manga.dict())
    if manga:
        return manga
    raise HTTPException(status_code=404, detail="Manga didn't found")


@man.put("/manga/{manga_id}")
async def update_manga(manga_id, manga: Manga):
    manga_collection.find_one_and_update({"_id": ObjectId(manga_id)},
                                         {"$set": jsonable_encoder(manga)})
    return {"message": f"updated {manga_id} successfully"}


@man.put("/manga/{manga_id}/chapter")
async def update_manga_chapter(chapter: Chapter):
    chapter = chapter.dict()
    manga_id = chapter["manga_id"]
    chapter_collection.insert_one(chapter)
    manga_collection.find_one_and_update({"_id": ObjectId(manga_id)},
                                         {"$push": {"chapters_id": manga_id}},
                                         upsert=True)
    return serialize_list(chapter_collection.find())
