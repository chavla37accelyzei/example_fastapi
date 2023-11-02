from sqlalchemy.orm import Session
from app.db.database import get_db
from fastapi import HTTPException, status,Depends
from datetime import datetime, timedelta
from typing import Optional

from app.controllers.user_controller import Hashing
from app.model.user_model import User

class User_Service():

    def add_user(self,data):
        db =next(get_db())
        try:
             db_user = User(
             Employee_id = data.Employee_id,
             First_name = data.First_name,
             Last_name = data.Last_name,
             email = data.email,
             password = data.password,
             PAN_number = data.PAN_number,
         )
             db.add(db_user)
             db.commit()
             db.refresh()
             return {"response": "user added successfully"}
        except Exception as e:
            db.rollback()
        finally:
            db.close
   
    

        

    
    



#getting user details

    def get_user(self,data):

        db =next(get_db())
        try:
          
          db_user = db.query(User).all()
          if db_user is None:
               
               raise HTTPException(status_code = 404,details = "user not found")
          
          
          return {"response": "user read succesfully"}  
        finally:
          db.close()   

     
     
     

   



   
    #filter(User.Employee_id = user_id).first()
    
    


def update_user(self,user_id,data):
    db =next(get_db())
    try:
        db_user=db.query(User).filter(User.Employee_id == user_id).first()
        db.add(db_user)
        db.commit()
        return db_user
        db.close()
    
    except:
        raise HTTPException(status_code = 404,details = "user not found")

        


def delete_user(self,user_id,data):
    
    db =next(get_db())
    try:
        db_user = db.query(User).filter(User.Employee_id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(db_user)
        db.commit()
        return {"user deleted succesfully"}
    finally:
        db.close()

