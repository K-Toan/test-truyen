from pydantic import BaseModel
from typing import Optional, List
from models.author import Author
from models.chapter import Chapter


class History(BaseModel):
    user_id: str
    history: Optional[str]


