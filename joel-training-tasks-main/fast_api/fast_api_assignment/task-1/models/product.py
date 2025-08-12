from sqlalchemy import Column,Integer,String,Float,TIMESTAMP,Uuid,DateTime
from db import Base
from datetime import datetime
class Product(Base):
    __tablename__ = "product"
    
    id = Column(Uuid,primary_key = True,index = True)
    name = Column(String(20))
    description = Column(String(200))
    price = Column(Float)
    category = Column(String(20))
    stock_quantity = Column(Integer)
    created_at = Column(TIMESTAMP,default=datetime.now())
    updated_at = Column(TIMESTAMP,onupdate=datetime.now()) 