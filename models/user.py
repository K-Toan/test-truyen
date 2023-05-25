from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    name: str
    username: str
    password: str
    history: Optional[List[str]]


