from pydantic import BaseModel


class UserLevel(BaseModel):  # User levels
    id: int
    name: str  # e.g., "admin", "operational", "final_user"
