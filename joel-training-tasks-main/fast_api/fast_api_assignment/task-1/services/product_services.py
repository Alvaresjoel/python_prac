from dependencies.get_db import get_db
from dto.product_dto import ProductDetails,CreateProduct,UpdatedDetail
from sqlalchemy.orm import Session
from models.product import Product
from fastapi import HTTPException,status
from datetime import datetime
from uuid import uuid4,UUID

class ProductService():
    def __init__(self,db:Session):
        self.db = db
        
    def create(self,new_item:ProductDetails):
        if self.db.query(Product).filter(Product.name == new_item.name).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product already exists")
        item = Product(
            id = uuid4(),
            name = new_item.name,
            description = new_item.description,
            price = new_item.price,
            category = new_item.category,
            stock_quantity = new_item.stock_quantity,
            created_at = datetime.now()
        )
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return CreateProduct(product_name=new_item.name,message = 'Item is added')
    
    
    def get_item(self,item_id:UUID):
        print(item_id)
        item = self.db.query(Product).filter(Product.id == item_id).first()
        if item is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product id doesnt exist")
        return item
    
    
    def get_item_all(self):
        return self.db.query(Product).all()
        
    def update_item(self,item_id:UUID,updated_details:UpdatedDetail):
        item = self.db.query(Product).filter(Product.id == item_id).first()        
        if item is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product id doesnt exist")
        item.category = updated_details.category
        item.price = updated_details.price
        item.stock_quantity = updated_details.stock_quantity
        item.updated_at = datetime.now()
        
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        
    def delete_item(self,item_id:UUID):
        item = self.db.query(Product).filter(Product.id == item_id).first()        
        if item is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Product id doesnt exist")
        self.db.query(Product).filter(Product.id == item_id).delete()
        self.db.commit()
        
    def get_item_by_category(self,category:str):
        items = self.db.query(Product).filter(Product.category == category).all()
        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found in this category")
        return items