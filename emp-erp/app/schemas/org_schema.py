from pydantic import BaseModel
from typing import List

class OrgBase(BaseModel):
    name: str = None
    logo: str = None
    corporate_address: str
    id : int = None

#class OrgCreate(OrgBase):
    #pass



    class Config:
        from_attributes = True