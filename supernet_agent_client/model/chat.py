from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Dict, List, Optional

class Chat(BaseModel):
    response_mode: str = ""
    conversation_id: str = ""
    files: List[str] = []
    query: str = ""
    inputs: Dict = {}
    config: Dict = Field(default_factory={}, alias="model_config")
    parent_message_id: Optional[str] = None

    @model_validator(mode='before')
    @classmethod
    def check_model_config(cls, data: Dict) -> Dict:
        print("Received data:", data)
        if isinstance(data, dict) and ('model_config' not in data or not data['model_config']):
            raise ValueError('model_config cannot be empty')
        print("AFTER Received data:", data)
        
        return data