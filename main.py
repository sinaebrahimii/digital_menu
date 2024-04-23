from fastapi import FastAPI
import models
from database import  engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
@app.get('/')
def read_root():
    return {"message": "Hello World"}