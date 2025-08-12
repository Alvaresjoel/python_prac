from typing import Optional
from pydantic import Field,BaseModel

class UserSignup(BaseModel):
    username :str = Field(min_length=5)
    email:str = Field(min_length=8)
    hashed_password : str = Field(min_length=8)
    role:str = Field(min_length=5)
class CreatedUser(BaseModel):
    message:str
    username:str

class UserSignin(BaseModel):
    email :str = Field(min_length=5)
    hashed_password : str = Field(min_length=8)


#FIXME
class Token(BaseModel):
    access_token:str
    refresh_token:str