from typing import Annotated
from fastapi import Depends, HTTPException,status
from jose import jwt,JWTError,ExpiredSignatureError
from uuid import UUID
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
load_dotenv()
import os 


def create_token(user_id:UUID,username:str,role:str,timelimit:timedelta,refresh:bool = False):
    encode = {'sub':username,'id':str(user_id),'role':role}
    token_timelimit = datetime.now(timezone.utc) + timelimit
    encode.update({'exp':token_timelimit}) 
    return jwt.encode(encode,key = os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))
    
     
def refresh_token(token:str):
    payload = jwt.decode(token,algorithms=os.getenv('ALGORITHM'),key = os.getenv('SECRET_KEY'))
    return create_token(payload['id'],payload['sub'],payload['role'],timedelta(seconds=20),refresh=True)    