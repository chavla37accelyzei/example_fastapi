from pydantic import BaseModel
from typing import List

class RoleBase(BaseModel):
    org_id: int
    role: str
    status: str

    class Config:
        from_attributes = True

