from typing import Optional
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
    price:Optional[float] = Field(None , gt = 1 )
    category:Optional[str] = Field(None,min_length=4)
    stock_quantity:Optional[int] = Field(None,ge=0)
    
class ProductParams(BaseModel):
    category:Optional[str] = Field(None,ge = 0)
    limit:Optional[int] = Field(None,ge = 0)
    page_no:Optional[int] = Field(None,ge = 1)