from pydantic import BaseModel
from typing import Optional, List, Any
import json

class UserHelper(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    roles: Optional[List[Any]] = None
    password:Optional[str] = None
    
    def to_dict(self):
        # Get the dictionary representation of the model and filter out None values
        self.convert_roles_to_dict()
        return {key: value for key, value in self.model_dump().items() if value is not None}

    def convert_roles_to_dict(self):
        self.roles = [
        {key: value for key, value in role.__dict__.items() if key != '_sa_instance_state'}
        for role in self.roles
        ]
