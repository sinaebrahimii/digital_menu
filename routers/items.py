from fastapi import APIRouter, HTTPException,Depends,Path
from sqlalchemy.orm import Session
from typing import Annotated,Union
from starlette import status
from models import Item,Category
from database import SessionLocal
from pydantic import BaseModel,Field

router = APIRouter(prefix="/items",tags=["items"])
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# database dependency injection
db_dependency= Annotated[Session , Depends(get_db)]

class ItemRequest(BaseModel):
    name:str
    price:int
    available:bool
    image_url:Union[str,None]=None
    category_id:int

@router.get("/{category_id}",status_code=status.HTTP_200_OK)
def read_items(db:db_dependency, category_id:int=Path(gt=0)):
    items=db.query(Item).filter(Category.id==category_id).all()
    if items is not None:
       return  items
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_item(db:db_dependency, item_request:ItemRequest):
    item=Item(**item_request.model_dump())
    db.add(item)
    db.commit()

