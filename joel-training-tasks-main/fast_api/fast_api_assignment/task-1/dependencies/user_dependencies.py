from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, Request, Response,status
from jose import jwt,ExpiredSignatureError
from uuid import UUID
from dotenv import load_dotenv
import os 

load_dotenv()
user_input_dependencies = Annotated[OAuth2PasswordRequestForm,Depends()]

oauth2_bearer = OAuth2PasswordBearer(tokenUrl = 'auth/sign-in')
token_header_dependencies = Annotated[str,Depends(oauth2_bearer)]


def verify_user_token(token:token_header_dependencies,request:Request):
    try:
        token = request.cookies.get("access_token") #or token
        payload = jwt.decode(token,algorithms=os.getenv('ALGORITM'),key = os.getenv('SECRET_KEY'))
        username:str = payload.get('sub')
        id : UUID = UUID(payload.get('id'))
        role :str = payload.get('role')
        if username is None or id is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail = 'Invalid user')
        return {'username':username,'id':id,'role':role}
    except ExpiredSignatureError :  
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail = 'Token Invalid')