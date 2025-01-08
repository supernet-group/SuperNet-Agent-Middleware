from pydantic import BaseModel

class BindingTag(BaseModel):
    target_id: str
    tag_ids: list[str]
    type: str = "app"
