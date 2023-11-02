from sqlalchemy import Column, String, Integer, DateTime, Date,ForeignKey, Boolean,VARCHAR,BigInteger
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

from app.model.orgs_model import Org
#Org is class,tablename = orgs


#locaation

class Location(Base):
    __tablename__ ="locations"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    org_id = Column(Integer,ForeignKey('orgs.id'),index = True)
    
    location = Column(String(length=30))
    location_head = Column(String(length=30))
    status = Column(String(length=40))

    # Relationship with Org table
    org  = relationship("Org" ,back_populates="locations" )
   