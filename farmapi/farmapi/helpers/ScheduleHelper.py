from pydantic import BaseModel
from typing import Optional, List

class ScheduleHelper(BaseModel):
    id: Optional[int] = None
    days_after_sowing: Optional[int] = None
    fertilizer: Optional[str] = None
    quantity: Optional[int] = None
    quantity_unit: Optional[str] = None
    farm_id: Optional[int] = None
    
    def to_dict(self):
        # Get the dictionary representation of the model and filter out None values
        return {key: value for key, value in self.model_dump().items() if value is not None}