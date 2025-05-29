from pydantic import BaseModel, Field

from app.schemas.category import Category


class RequestEmbedding(BaseModel):
    id: int = Field(description="The id of the document")
    title: str = Field(description="The title of the document")
    body: str = Field(description="The HTML body of the document")
    categories: list[Category] = Field(description="The categories of the document")
