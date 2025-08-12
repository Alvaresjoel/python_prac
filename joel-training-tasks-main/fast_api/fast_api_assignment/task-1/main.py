from fastapi import FastAPI
from db import engine,Base
from models import product,user
from routes import product_routes,user_routes
import uvicorn 

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(product_routes.router)
app.include_router(user_routes.router)
 
if __name__  == '__main__':
        uvicorn.run(app,host = '127.0.0.1',port = 5000)
