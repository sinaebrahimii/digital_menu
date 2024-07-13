from fastapi import APIRouter, HTTPException,Depends,Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Annotated,Union,List
from starlette import status
from models import Item,Category,Option
from database import SessionLocal
from pydantic import BaseModel,Field
from schemas import schemas
router = APIRouter(prefix="/items",tags=["items"])
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# database dependency injection
db_dependency= Annotated[Session , Depends(get_db)]

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ItemResponse])
async def read_all_items(db:db_dependency):
    items = db.query(Item).all()
    if items is not None:
        return  items
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/{item_id}",status_code=status.HTTP_200_OK,response_model=schemas.ItemResponse)
async def read_items(db:db_dependency, item_id:int=Path(gt=0)):
    item=db.query(Item).filter(Item.id==item_id).first()
    if item is not None:
       return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ItemResponse)
async def create_item(db:db_dependency, item_request:schemas.ItemRequest):
    item=Item(**item_request.model_dump())
    db.add(item)
    db.commit()
    return item

@router.post("/options/{item_id}",status_code=status.HTTP_201_CREATED,)
async def create_options(db:db_dependency,option_request:schemas.OptionRequest,item_id:int=Path(gt=0)):
    option=Option(name=option_request.name,price=option_request.price,item_id=item_id)
    db.add(option)
    db.commit()

@router.put("/{item_id}",status_code=status.HTTP_200_OK,response_model=schemas.ItemResponse)
async def update_item(db:db_dependency, item_request:schemas.ItemRequest,item_id:int=Path(gt=0)):
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

@router.delete('/{item_id}',status_code=status.HTTP_200_OK)
async def delete_item(db:db_dependency,item_id:int=Path(gt=0)):
    item_to_delete=db.query(Item).filter(Item.id==item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(item_to_delete)
    db.commit()
    return {"message": "Item deleted successfully"}

    
