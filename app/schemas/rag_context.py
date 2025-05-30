from typing import List

from pydantic import BaseModel, Field


class RagContext(BaseModel):
    has_results: bool
    list_of_topics_ids: List[int]
    list_of_topics_titles: List[str]
    formatted_contents: List[str]
    message: str
