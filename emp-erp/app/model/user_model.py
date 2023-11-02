from sqlalchemy import Column, String, Integer, DateTime, Date,ForeignKey, Boolean,VARCHAR,BigInteger
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

from app.model.orgs_model import Org
#Orgs is class, tablename="orgs"


class User(Base):
    __tablename__ ="user"
    Employee_id = Column(Integer, primary_key=True, autoincrement=True) 
    org_id = Column(Integer,  index=True)
    First_name = Column(String(30))
    Last_name = Column(String(30))
    email = Column(String(length=40),unique=True, index=True)
    password = Column(String(length=40),unique=True)
    Date_of_birth = Column(Date)
    Join_date = Column(Date)
    Department = Column(String(30))
    Role_id = Column(Integer)
    Reporting_Manager_id = Column(Integer)
    status = Column(String(50))
    Location = Column(String(50))
    PAN_number = Column(String(length=12),unique=True)  # fixwd 10 unique
    UAN_number = Column(String(length=12))             # fixed unqiue 12 
   
    PF_number = Column(String(length=15),unique=True)  # fixed 15 digit unque
       
    Bank_account_number = Column(String(length=20),unique=True)   # max length of 20 char
    updated_date  = Column(DateTime, default=datetime.utcnow)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_by = Column(Integer,ForeignKey("user.id"))
    created_by = Column(Integer,ForeignKey("user.id"))

    org = relationship("Org",back_populates="user")
'''
    Department
Role_id
Reporting_Manager_id
status
Location
PAN Number
UAN Number
PF Number
Bank A/C Number
updated_date
updated_by
created_date
created_by


    
'''