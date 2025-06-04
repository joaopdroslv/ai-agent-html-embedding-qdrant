from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int
    name: str
    description: str
