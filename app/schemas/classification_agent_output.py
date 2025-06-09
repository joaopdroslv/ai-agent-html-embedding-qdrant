from pydantic import BaseModel


class ClassificationAgentOutput(BaseModel):
    has_category: bool = False
    category_id: str = None
    category_name: str = None
