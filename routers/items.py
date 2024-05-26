from fastapi import APIRouter, HTTPException,Depends,Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Annotated,Union
from starlette import status
from models import Item,Category,Option
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

class OptionRequest(BaseModel):
    name:str
    price:int

class ItemResponse(BaseModel):
    id:Union[int,None]=None
    name:str
    price:int
    available:bool
    image_url:Union[str,None]=None
    category_id:int

@router.get("/{category_id}",status_code=status.HTTP_200_OK)
async def read_items(db:db_dependency, category_id:int=Path(gt=0)):
    items=db.query(Item).filter(Item.category_id==category_id).all()
    for i in items:
        print (i.options)
    if items is not None:
       return  items
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_item(db:db_dependency, item_request:ItemRequest):
    item=Item(**item_request.model_dump())
    db.add(item)
    db.commit()

@router.post("/options/{item_id}",status_code=status.HTTP_201_CREATED)
async def create_options(db:db_dependency,option_request:OptionRequest,item_id:int=Path(gt=0)):
    option=Option(name=option_request.name,price=option_request.price,item_id=item_id)
    db.add(option)
    db.commit()

@router.put("/{item_id}",status_code=status.HTTP_200_OK,response_model=ItemResponse)
async def update_item(db:db_dependency, item_request:ItemRequest,item_id:int=Path(gt=0)):
    item=db.query(Item).filter(Item.id==item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    item.name=item_request.name
    item.price=item_request.price
    item.available=item_request.available
    item.image_url=item_request.image_url
    item.category_id=item_request.category_id
    db.add(item)
    db.commit()
    return item

@router.delete('/{item_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(db:db_dependency,item_id:int=Path(gt=0)):
    item=db.query(Item).filter(Item.id==item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.query(Item).filter(Item.id==item_id).delete()
    db.commit()
    
