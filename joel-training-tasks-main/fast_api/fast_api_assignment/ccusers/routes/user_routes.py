from fastapi import APIRouter,Depends,status
from dependencies.get_db import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from services.user_service import UserService
from dto.users_dto import SignupRequest   
 
db_dependencies = Annotated[Session,Depends(get_db)]

router = APIRouter(
    prefix= '/user',
    tags= ['user']
)

@router.post("/user_create",status_code=status.HTTP_201_CREATED)
async def signup(sign_up_request:SignupRequest,db:db_dependencies):
    return UserService(db).signup_user(sign_up_request)