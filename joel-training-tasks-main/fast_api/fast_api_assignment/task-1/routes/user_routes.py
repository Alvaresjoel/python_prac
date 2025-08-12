from typing import Annotated
from auth.token import create_token
from dto.users_dto import UserSignin,UserSignup
from fastapi import APIRouter, Depends, Response ,status,HTTPException
from dependencies.get_db import get_db
from dependencies.user_dependencies import user_input_dependencies,verify_user_token,token_header_dependencies
from services.user_services import UserService
from sqlalchemy.orm import Session
user_dependencies = Annotated[token_header_dependencies,Depends(verify_user_token)]
from starlette.requests import Request
from auth.token import refresh_token
db_dependencies = Annotated[Session,Depends(get_db)]
# user_dependencies = Annotated[token_header_dependencies,Depends(verify_user_token)]

router = APIRouter(
    prefix="/auth",
    tags = ['auth']
)

@router.post('/sign-up',status_code=status.HTTP_201_CREATED)
def signup(db:db_dependencies,user_request :UserSignup):
    try:
        return UserService(db).signup_user(user_request)
    except HTTPException as error:
        raise(error)

@router.post('/sign-in',status_code=status.HTTP_201_CREATED)
def signin(db:db_dependencies,user_request :user_input_dependencies,response:Response):
    try:
        return UserService(db).signin_user(user_request,response)
    except HTTPException as error:
        raise (error)

@router.get('/refresh-token')
def new_access_token(request:Request,response:Response):
    try:
        token = request.cookies.get("refresh_token")
        if token is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token not found")
        new_access_token = refresh_token(token)
        response.set_cookie(key="access_token", value=new_access_token, httponly=True)
        return {"access_token": new_access_token, "token_type": "bearer"}
    except HTTPException as error:
        raise error
