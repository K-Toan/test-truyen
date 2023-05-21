from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["test_truyen"]
manga_collection = db["manga"]
author_collection = db["author"]
