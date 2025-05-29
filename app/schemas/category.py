from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int = Field(description="The id of the category")
    name: str = Field(description="The name of the category")
    description: str = Field(description="The description of the category")
