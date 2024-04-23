from fastapi import APIRouter, HTTPException,Depends,Path
from sqlalchemy.orm import Session
from typing import Annotated,Union
from starlette import status
from models import Item,Category
from database import SessionLocal
from pydantic import BaseModel,Field

router = APIRouter(prefix="/categories",tags=["categories"])
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# database dependency injection
db_dependency= Annotated[Session , Depends(get_db)]

class CategoryRequest(BaseModel):
    name:str
@router.get("/",status_code=status.HTTP_200_OK)
def read_categories(db:db_dependency):
    categories=db.query(Category).all()
    if len(categories) is not 0:
       return  categories
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_category(db:db_dependency, category_request: CategoryRequest):
    category=Category(name=category_request.name)
    db.add(category)
    db.commit()