from sqlalchemy import Column, String, Integer, DateTime, Date,ForeignKey, Boolean,VARCHAR,BigInteger
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

from app.model.orgs_model import Org
#Orgs is class,  tablename=orgs 

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    org_id = Column(Integer,ForeignKey('orgs.id'), index=True)
   
    role = Column(String)
    status = Column(String)

    # Relationship with Org table
    org = relationship("Org", back_populates="roles")
