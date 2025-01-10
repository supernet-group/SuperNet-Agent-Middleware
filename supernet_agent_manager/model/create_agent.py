from pydantic import BaseModel

class CreateAgent(BaseModel):
    name: str
    short_name: str = ""
    description: str
    tags: list[str] = []
    icon: str
    icon_type: str
    icon_background: str
    mode: str = "agent-chat" # "agent-chat" or "yaml-content"
    yaml_content: str = None