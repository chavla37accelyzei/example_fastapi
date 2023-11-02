from sqlalchemy.orm import Session
from app.db.database import get_db
from fastapi import HTTPException, status,Depends
from datetime import datetime, timedelta
from typing import Optional

from app.controllers.location_controller import Hashing
from app.model.location_model import Location

class Location_Service():

    def add_location(self,data):
        db =next(get_db())
        try:
             db_location = Location(
             Employee_id = data.Employee_id,
             First_name = data.First_name,
             Last_name = data.Last_name,
             email = data.email,
             password = data.password,
             PAN_number = data.PAN_number,
         )
             db.add(db_location)
             db.commit()
             db.refresh()
             return {"response": "location added successfully"}
        except Exception as e:
            db.rollback()
        finally:
            db.close
   
    

        

    
    



#getting user details

    def get_location(self,data):

        db =next(get_db())
        try:
          
          db_user = db.query(Location).all()
          if db_user is None:
               
               raise HTTPException(status_code = 404,details = "location not found")
          
          
          return {"response": "location read succesfully"}  
        finally:
          db.close()   

     
     
     

   



   
    #filter(User.Employee_id = user_id).first()
    
    

    
def update_location(self,id,data):
    db =next(get_db())

    try:
        db_location=db.query(Location).filter(db =next(get_db()).Employee_id == id).first()
        db.add(db_location)
        db.commit()
        return {"response":"location updated succesfully"}
        db.close()
    
    except:
        raise HTTPException(status_code = 404,details = "location not found")

    

def delete_user(self,user_id,data):
    
    db =next(get_db())
    try:
        db_user = db.query(Location).filter(Location.Employee_id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="location not found")
        db.delete(db_user)
        db.commit()
        return {"location deleted succesfully"}
    finally:
        db.close()

