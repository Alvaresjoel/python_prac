from typing import Annotated
from sqlalchemy.orm import Session
from dto.product_dto import ProductDetails,UpdatedDetail,ProductParams
from fastapi import APIRouter,Depends ,status,HTTPException
from dependencies.get_db import get_db
from services.product_services import ProductService
from uuid import UUID
from dependencies.user_dependencies import token_header_dependencies,verify_user_token

db_dependencies = Annotated[Session,Depends(get_db)]
user_dependencies = Annotated[token_header_dependencies,Depends(verify_user_token)]


router = APIRouter(
    prefix = '/products',
    tags = ['products']
)
@router.get('/')
async def get_all_products(
    db:db_dependencies,
    user:user_dependencies,
    params:ProductParams = Depends()
    ):
    try:
        if user is None :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User')
        if params.category is not None:
            return ProductService(db).get_item_by_category(params)    
        return ProductService(db).get_item_all(params)
    except HTTPException as error:
        raise(error)
    
@router.get('/price')
async def get_product_by_price(lower_range:int,upper_range:int,db:db_dependencies,user:user_dependencies):
    try:
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User')
        return ProductService(db).get_item_in_price_range(lower_range,upper_range)
    except HTTPException as error:
        raise(error)

# @router.get('/')
# async def get_products_by_category(db:db_dependencies,user:user_dependencies,category:str|None = None):
#     try:
#         if user is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User')
#         return ProductService(db).get_item_by_category(category)    
#     except HTTPException as error:
#         raise(error)
    
@router.get('/{id}')
async def get_product_by_id(id:UUID,db:db_dependencies,user:user_dependencies):
    try:
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User')
        return ProductService(db).get_item(id)
    except HTTPException as error:
        raise(error)


@router.post('/',status_code = status.HTTP_201_CREATED)
async def create_new_product(new_item:ProductDetails,db:db_dependencies,user:user_dependencies):
    try:
        if user is None or user.get('role') != 'admin':
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Unauthorised Route')
        return ProductService(db).create(new_item)
    except HTTPException as error:
        raise(error)

@router.patch('/{id}')
async def update_product(id:UUID,updated_details:UpdatedDetail,db:db_dependencies,user:user_dependencies) -> None:
    try:
        if user is None or user.get('role') != 'admin':
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Unauthorised Route')
        return ProductService(db).update_item(id,updated_details)
    except HTTPException as error:
        raise(error)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id:UUID,db:db_dependencies,user:user_dependencies): 
    try:
        if user is None or user.get('role') != 'admin':
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Unauthorised Route')
        return ProductService(db).delete_item(id)
    except HTTPException as error:
        raise(error)

    
