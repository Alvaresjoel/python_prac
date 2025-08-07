from fastapi import FastAPI
from db import engine, Base
import models.users
from routes import user_routes 
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routes.router)