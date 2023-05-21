from pydantic import BaseModel
from typing import Optional, List
from models.author import Author
from models.chapter import Chapter


class Manga(BaseModel):
    name: str
    author_id: Optional[str]
    genres: List[str]
    chapters: List[Chapter]


