from pydantic import BaseModel,Field

class SignupRequest(BaseModel):
    username:str
    password:str
    # age:str = Field(gt = 0)
    
class SignupResponse(BaseModel):
    username:str
    message:str 