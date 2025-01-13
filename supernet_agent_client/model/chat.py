from pydantic import BaseModel

class Chat(BaseModel):
    conversation_id: str
    parent_message_id: str
    query: str
    files: list[str]
    inputs: list[str]
    response_mode: str = "streaming"
