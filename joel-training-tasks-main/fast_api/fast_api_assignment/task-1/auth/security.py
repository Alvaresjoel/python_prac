from fastapi import HTTPException,status
from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'],deprecated = ['auto'])

def hash_password(password:str):
    return context.hash(password)

def verify_password(hashed_password:str,user_password:str):
    return context.verify(user_password,hashed_password)

