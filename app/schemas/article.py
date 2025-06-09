from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int
    title: str


class Article(ArticleBase):
    # Represents the article with it's content in markdown
    content: str
