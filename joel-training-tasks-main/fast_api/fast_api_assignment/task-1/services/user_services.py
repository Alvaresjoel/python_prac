from urllib import response
from dto.users_dto import UserSignup,CreatedUser,UserSignin
from sqlalchemy.orm import Session
from models.user import Users
from fastapi import HTTPException, Response,status
from datetime import timedelta
from auth import security
from auth.token import create_token
from dependencies.user_dependencies import user_input_dependencies

class UserService():
    def __init__(self,db:Session):
        self.db = db
        
    def signup_user(self,user:UserSignup):
        try:
            if self.db.query(Users).filter(Users.email == user.email).first():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product already exists")
            new_user = Users(
                username = user.username,
                hashed_password = security.hash_password(user.hashed_password),
                email = user.email,
                role = user.role
                )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)  
            return CreatedUser(message = 'User successfully added',username = new_user.username)
        
        except HTTPException as error:
            raise error
        
    def signin_user(self,user:user_input_dependencies,response:Response):
        try:
            item = self.db.query(Users).filter(Users.email == user.username).first() 
            if item is None :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Email doesnt exist")
            if not security.verify_password(item.hashed_password,user.password) :
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail = "Invalid password")
           
            access_token = create_token(item.id,item.username,item.role,timedelta(seconds=20))
            refresh_token = create_token(item.id,item.username,item.role,timedelta(hours=2))
            response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
            response.set_cookie(key="access_token", value=access_token, httponly=True)
            return {
                    'access_token':access_token,
                    'token_type':'bearer',
                    
                    }
        except TypeError as error:
            raise error
        except HTTPException as error :
            raise error
        
    
        
    