from pydantic import BaseModel
from typing import Optional, List, Any
from farmapi.models import Farm
class FarmerHelper(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    language: Optional[str] = None
    farms: Optional[List[Any]] = None
    
    def to_dict(self):
        # Get the dictionary representation of the model and filter out None values
        return {key: value for key, value in self.model_dump().items() if value is not None}