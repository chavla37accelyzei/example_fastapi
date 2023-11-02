from sqlalchemy import Column, String, Integer, DateTime, Date,ForeignKey, Boolean,VARCHAR,BigInteger
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime



# Org Table
class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=30))
    logo = Column(String(length=30))  # Assuming a string path to the logo file
    corporate_address = Column(String(length=30))

# Relationship with Location and Role tables
    locations = relationship("location", back_populates="org")
    user = relationship("user" , back_populates="Org")
    roles = relationship("Role", back_populates="org")