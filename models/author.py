from typing import Optional
from pydantic import BaseModel


class Author(BaseModel):
    name: str
    bio: Optional[str]

