from pydantic import BaseModel, Field

from app.schemas.category import Category
from app.schemas.user_level import UserLevel


class RequestEmbedding(BaseModel):
    id: int
    title: str
    body: str
    categories: list[Category]
    levels: list[UserLevel]
