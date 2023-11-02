
from fastapi import  Depends , HTTPException, APIRouter
from sqlalchemy.orm import Session


# in this controller we have to import model(table class(),schema(schema class)
from app.db.database import Base,get_db
from app.model.location_model import Location
from app.schemas.location_schema import LocationBase
from app.services.location_service import Location_Service

router = APIRouter(prefix="/api")

Location_Service=Location_Service()
# Create User


# using routers
@router.post("/users")
def add_user(data:LocationBase):
    response = Location_Service.add_location(data)
    return response

@router.get("/users")
def get_users():
    response = Location_Service.get_location()
    return response   

@router.put("/users/{id}")
def update_user(id:int, data:LocationBase):
    response = Location_Service.update_user(id,data)
    return response   

@router.delete("/users/{id}")
def delete_user(id: int, data: LocationBase):
    response = Location_Service.delete_user(id, data)
    return response