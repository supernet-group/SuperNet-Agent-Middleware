from pydantic import BaseModel,Field
from typing import Optional, Dict, Any

class GenericAPIRequest(BaseModel):
    url: str  # request URL
    method: str  # request method （GET、POST、PUT、DELETE ）
    headers: Optional[Dict[str, str]] = None  
    params: Optional[Dict[str, Any]] = None  # query parameters （GET req）
    data: Optional[Dict[str, Any]] = None  # form data （POST req）
    json_data: Optional[Dict[str, Any]] =  Field(default=None, alias="json")  # JSON data（POST req）