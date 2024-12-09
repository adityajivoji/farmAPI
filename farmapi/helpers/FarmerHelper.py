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
        self.convert_farm_to_dict()
        print(self.farms)
        return {key: value for key, value in self.model_dump().items() if value is not None}
    
    def convert_farm_to_dict(self):
        self.farms = [
        {key: value for key, value in farm.__dict__.items() if key != '_sa_instance_state'}
        for farm in self.farms
        ]
