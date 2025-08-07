from pydantic import BaseModel,Field

class ProductDetails(BaseModel):
    name:str = Field(min_length=4)
    description :str = Field(min_length=4)
    price :float = Field(gt=0)
    category : str = Field(min_length=4)
    stock_quantity :int = Field(ge=0)
    
class CreateProduct(BaseModel):
    product_name:str
    message:str
    
class UpdatedDetail(BaseModel):
    price:float = Field(gt=0)
    category:str = Field(min_length=4)
    stock_quantity:int = Field(ge=0)