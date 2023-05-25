from fastapi import APIRouter
from models.author import Author
from schemas.schema import *
from bson import ObjectId
from config import *

aut = APIRouter()


@aut.get("/author")
async def get_author():
    return serialize_list(author_collection.find())


@aut.get("/author/{author_id}")
async def get_author_by_id(author_id):
    return serialize_dict(author_collection.find_one({"_id": ObjectId(author_id)}))


@aut.post("/author")
async def create_author(author: Author):
    author_collection.insert_one(dict(author))
    return serialize_list(author_collection.find())


@aut.put("/author/{author_id}")
async def update_author(author_id, author: Author):
    author_collection.find_one_and_update({"_id": ObjectId(author_id)},
                                          {"$set": dict(author)})
    return serialize_dict(author_collection.find_one({"_id": ObjectId(author_id)}))
