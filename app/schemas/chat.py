from pydantic import BaseModel


class RagRetrieve(BaseModel):
    question: str


class ChatQuestion(BaseModel):
    question: str
    level: int  # Represents the agent level


class LevelContext(BaseModel):
    level: int
