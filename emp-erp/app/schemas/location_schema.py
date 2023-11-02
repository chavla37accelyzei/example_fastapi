from pydantic import BaseModel
from typing import List

class LocationBase(BaseModel):
    org_id: int
    location: str
    location_head: str
    status: str
    id:int

    class Config:
        from_attributes = True