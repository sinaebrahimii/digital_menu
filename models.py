from database import Base
from sqlalchemy import Column , Integer, String,Boolean,ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'items'
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String,unique=True)
    price=Column(Integer)
    available=Column(Boolean,default=True)
    image_url=Column(String)
    category_id=Column(Integer, ForeignKey('categories.id'))
    options = relationship("Option", back_populates="item")
    category=relationship("Category", back_populates="items")


class Option(Base):
    __tablename__ = 'options'
    id=Column(Integer, primary_key=True,index=True)
    price=Column(Integer)
    item_id=Column(Integer, ForeignKey('items.id'))
    item=relationship("Item", back_populates="options")

class Category(Base):
    __tablename__ = 'categories'
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String,unique=True)
    items=relationship("Item", back_populates="category")

class User(Base):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True)
    role=Column(String)
    password=Column(String)