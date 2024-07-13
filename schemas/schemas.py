from pydantic import BaseModel
from typing import List
class ItemRequest(BaseModel):
    name:str
    price:int
    available:bool
    image_url:str|None=None
    category_id:int

class OptionRequest(BaseModel):
    name:str
    price:int


class OptionResponse(BaseModel):
    id:int|None=None
    item_id:int
    name:str
    price:int
    class Config:
        orm_mode = True

class ItemResponse(BaseModel):
    id:int|None=None
    name:str
    price:int
    available:bool
    image_url:str|None=None
    category_id:int|None
    options:List[OptionResponse]
    class Config:
        orm_mode = True