from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime
class FarmHelper(BaseModel):
    id: Optional[int] = None
    area: Optional[str] = None
    crop_grown: Optional[str] = None
    sowing_date: Optional[datetime] = None
    village: Optional[str] = None
    farmer_id: Optional[int] = None
    schedule: Optional[List[Any]] = None
    
    def to_dict(self):
        self.convert_schedule_to_dict()
        return {key: value for key, value in self.model_dump().items() if value is not None}
    
    def convert_schedule_to_dict(self):
        self.schedule = [
        {key: value for key, value in s.__dict__.items() if key != '_sa_instance_state'}
        for s in self.schedule
        ]