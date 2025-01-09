from pydantic import BaseModel, Field

class ListAgents(BaseModel):
    name: str = Field(default='', min_length=0, max_length=100)
    page: int
    limit: int