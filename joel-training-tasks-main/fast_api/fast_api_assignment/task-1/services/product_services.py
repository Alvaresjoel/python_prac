from dependencies.get_db import get_db
from dto.product_dto import ProductDetails,CreateProduct, ProductParams,UpdatedDetail
from sqlalchemy.orm import Session
from models.product import Product
from fastapi import HTTPException,status
from datetime import datetime
from uuid import uuid4,UUID
class ProductService():
    def __init__(self,db:Session):
        self.db = db
        
    def create(self,new_item:ProductDetails) -> CreateProduct:
        try:
            if self.db.query(Product).filter(Product.name == new_item.name).first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product already exists")
            item = Product(
                id = uuid4(),
                name = new_item.name,
                description = new_item.description,
                price = new_item.price,
                category = new_item.category,
                stock_quantity = new_item.stock_quantity,
                # created_at = datetime.now()
            )
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)
            return CreateProduct(product_name=new_item.name,message = 'Item is added')
        except HTTPException as error:
            raise error
    
    def get_item(self,item_id:UUID) ->list[Product]:
        try:
            item = self.db.query(Product).filter(Product.id == item_id).first()
            if item is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product id doesnt exist")
            return item
        except HTTPException as error:
            raise error
    
    def get_item_all(self,params:ProductParams) ->list[Product]:
        try:
            query = self.db.query(Product).order_by(Product.name)
            if params.page_no is None or params.limit is None:
                return query.all()
            offset = (params.page_no - 1) * params.limit
            return query.limit(params.limit).offset(offset).all()
        except HTTPException as error:
            raise error
        
    def update_item(self,item_id:UUID,updated_details:UpdatedDetail):
        try:
            item = self.db.query(Product).filter(Product.id == item_id).first()        
            if item is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product id doesnt exist")
            update_dict = updated_details.model_dump(exclude_unset= True)
            item = self.db.query(Product).filter(Product.id == item_id).\
            update(update_dict)
            # item.updated_at = datetime.now()
            self.db.commit()
        except HTTPException as error:
            raise error
        
    def delete_item(self,item_id:UUID):
        try:
            item = self.db.query(Product).filter(Product.id == item_id).first()        
            if item is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product id doesnt exist")
            self.db.query(Product).filter(Product.id == item_id).delete()
            self.db.commit()
        except HTTPException as error:
            raise error
            
    def get_item_by_category(self,params:ProductParams) ->list[Product] :
        try:
            items = self.db.query(Product).filter(Product.category == params.category).all()
            if items is None :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found in this category")
            return items    
        except HTTPException as error:
            raise error
        
    def get_item_in_price_range(self,lower_range:int,upper_range:int)->list[Product]:
        try:
            items = self.db.query(Product).filter(Product.price < upper_range,Product.price > lower_range).all()
            if items is None :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found in this category")
            return items
        except HTTPException as error:
            raise (error)
        
        