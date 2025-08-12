from db import Base
from sqlalchemy import Column,Integer,String,Float,TIMESTAMP,Uuid,DateTime
from datetime import datetime
import uuid
class Users(Base):
    __tablename__ = "users"
    id = Column(Uuid,primary_key = True,index = True,default=uuid.uuid4)
    username = Column(String(50))
    hashed_password = Column(String(255))
    email = Column(String(35),unique=True)
    role = Column(String(35))