from fastapi import FastAPI
import models
from database import  engine
from routers import items,categories

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(items.router)
app.include_router(categories.router)
@app.get('/')
def read_root():
    return {"message": "Hello World"}