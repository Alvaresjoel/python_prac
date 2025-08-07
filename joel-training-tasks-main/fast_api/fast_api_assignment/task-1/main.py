from fastapi import FastAPI
from db import engine,Base
from models import product
from routes import product_routes
# print(Base)
product.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(product_routes.router)
import uvicorn # type: ignore
 
if __name__  == '__main__':
        uvicorn.run(app,host = '127.0.0.1',port = 5000)
