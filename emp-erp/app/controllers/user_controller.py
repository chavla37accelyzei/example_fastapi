
from fastapi import  Depends , APIRouter, HTTPException, status



# in this controller we have to import model(table class(),schema(schema class)
from app.db.database import Base,get_db
from app.model.user_model import User
from app.schemas.user_schema import CreateUser,UpdateUser,StatusChange,userresponse

from app.services.user_service import User_Service

# Create User
router = APIRouter(prefix="/api")

user_service = User_Service()


# using routers
@router.post("/users")
def add_user(data:CreateUser):
    response = user_service.add_user(data)
    return response

@router.get("/users")
def get_users():
    response = user_service.get_users()
    return response   

@router.put("/users/{id}")
def update_user(id:int, data:StatusChange):
    response = user_service.update_user(id,data)
    return response   

@router.delete("/users/{id}")
def delete_user(id: int, data: StatusChange):
    response = user_service.delete_user(id, data)
    return response