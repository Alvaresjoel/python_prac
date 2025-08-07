from dto.product_dto import ProductDetails,UpdatedDetail
from fastapi import APIRouter ,status,HTTPException
from dependencies.get_db import db_dependencies
from services.product_services import ProductService
from uuid import UUID
router = APIRouter(
    prefix = '/products',
    tags = ['products']
)



@router.get('/')
async def get_all_products(db:db_dependencies):
    return ProductService(db).get_item_all()


@router.get('/{id}')
async def get_product_by_id(id:UUID,db:db_dependencies):
    return ProductService(db).get_item(id)



@router.post('/',status_code = status.HTTP_201_CREATED)
async def create_new_product(new_item:ProductDetails,db:db_dependencies):
    return ProductService(db).create(new_item)



@router.patch('/{id}')
async def update_product(id:UUID,updated_details:UpdatedDetail,db:db_dependencies) -> None:
    return ProductService(db).update_item(id,updated_details)



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id:UUID,db:db_dependencies): 
    return ProductService(db).delete_item(id)

@router.get('/category/')
async def get_products_by_category(category:str, db:db_dependencies):
    return ProductService(db).get_item_by_category(category)