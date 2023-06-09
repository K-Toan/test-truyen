from pydantic import BaseModel
from typing import Optional, List
from models.author import Author
from models.chapter import Chapter


class Manga(BaseModel):
    name: str
    genres: List[str]
    author_id: Optional[str]
    chapters_id: Optional[List[str]]


