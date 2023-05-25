from fastapi import FastAPI
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["test_truyen"]
manga_collection = db["manga"]
author_collection = db["author"]
user_collection = db["user"]
chapter_collection = db["chapter"]
