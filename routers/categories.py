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
async def read_categories(db:db_dependency):
    categories=db.query(Category).all()
    if len(categories) != 0:
       return  categories
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_category(db:db_dependency, category_request: CategoryRequest):
    category=Category(name=category_request.name)
    db.add(category)
    db.commit()

@router.delete('/{category_id}',status_code=status.HTTP_200_OK)
async def delete_category(db:db_dependency, category_id:int=Path(gt=0)):
    category = db.query(Category).filter(Category.id==category_id).first()
    if category is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    db.query(Category).filter(Category.id == category_id).delete()
    db.commit()