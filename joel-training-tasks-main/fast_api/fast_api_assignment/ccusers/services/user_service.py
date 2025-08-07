from fastapi import HTTPException,status
from auth.security import hash_password
from models.users import Users
from dto.users_dto import SignupRequest,SignupResponse
from sqlalchemy.orm import Session

class UserService():
    def __init__(self,db:Session):
        self.db = db
        
    def signup_user(self,signup_request:SignupRequest)->SignupResponse:
        if self.db.query(Users).filter(Users.username == signup_request.username).first():
            raise HTTPException(status_code=status.HTTP_400,detail="User already exists in db")
        new_user  = Users(
                username = signup_request.username,
                hashed_password = hash_password(signup_request.password)
            )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return SignupResponse(username = signup_request.username,message="Successfully saved user to database")