from pydantic import BaseModel
from typing import Optional, List, Any


class UserHelper(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    roles: Optional[List[Any]] = None
    password:Optional[str] = None
    
    def to_dict(self):
        # Get the dictionary representation of the model and filter out None values
        return {key: value for key, value in self.model_dump().items() if value is not None}
