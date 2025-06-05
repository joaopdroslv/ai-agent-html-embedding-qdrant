from typing import List

from pydantic import BaseModel, Field


class SimilarityScore(BaseModel):
    topic_id: int
    topic_title: str
    similarity_score: float


class RagContext(BaseModel):
    has_results: bool
    list_of_topics_ids: List[int]
    list_of_topics_titles: List[str]
    formatted_contents: List[str]
    similarity_scores: List[SimilarityScore]
    message: str
