from pydantic import BaseModel, Field


class AnswererAgentOutput(BaseModel):
    answer: str
    has_related_topics: bool = False
    list_of_topics_ids: list[int] = []
    list_of_topics_titles: list[str] = []
    tools_used: list[str] = []
