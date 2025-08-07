from sqlalchemy import Column, Integer , String
from db import Base
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key= True,index = True, autoincrement = "auto")
    username = Column(String(20),unique = True, index = True)
    hashed_password = Column(String(255))
    age = Column(Integer)