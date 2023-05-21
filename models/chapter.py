from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class Chapter(BaseModel):
    number: int
    title: str
    publish_date: datetime
    pages: List[str]
    comments: Optional[List[str]]
