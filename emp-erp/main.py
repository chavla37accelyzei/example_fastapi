from fastapi import FastAPI ,Depends , HTTPException
from starlette.middleware.cors import CORSMiddleware
#from sqlalchemy.orm import Session
#from dotenv import load_dotenv

from app.controllers.user_controller import router as user_details
from app.controllers.location_controller import router as location_router
from app.controllers.role_controller import router as role_router

from app.db.database import Base,get_db
from app.model.user_model import User
from app.model.location_model import Location
from app.schemas.user_schema import CreateUser,UpdateUser,StatusChange,userresponse



app = FastAPI()


app.include_router(user_details, prefix="/users", tags=["users"])
app.include_router(location_router, prefix="/locations", tags=["locations"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get('/')
async def home():
	return "Application Running..."

'''
@app.post("/user",response_model=userresponse)
# user: dervies CreateUser BaseModel
def create_user(user:CreateUser,db = Depends(get_db)):
    db_user = User(
        Employee_id = user.Employee_id,
        First_name = user.First_name,
        Last_name = user.Last_name,
        email = user.email,
        password = user.password,
        PAN_number = user.PAN_number,


    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    db.close()



#getting user details
@app.get("/user/{user_id}",response_model=userresponse)
def get_user(user_id:int,db = Depends(get_db)):
    db_user = db.query(User).all()
    #filter(User.Employee_id = user_id).first()
    if db_user is None:
        raise HTTPException(status_code = 404,details = "user not found")
    return db_user
'''