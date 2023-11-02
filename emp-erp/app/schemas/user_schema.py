from pydantic import BaseModel
from datetime import datetime
from typing import List

# add schema
class CreateUser(BaseModel):
    Employee_id : int = None
    First_name : str = None
    Last_name : str = None
    email : str 
    password : str 
    PAN_number:str = None
    UAN_number:str = None
    Bank_account_number:str = None
    created_by : int = None

class userresponse(CreateUser):
    Employee_id:int 
    First_name:str
    email :str

class UpdateUser(BaseModel):
    Employee_id : int = None
    First_name : str = None
    Last_name : str = None
    email : str
    password : str 
    PAN_number:str = None
    UAN_number:str = None
    Bank_account_number:str = None
    

class StatusChange(BaseModel):
    updated_by:int=None
    status : str = None   


    class Config:
        from_attributes = True
