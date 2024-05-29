from database import Base
from sqlalchemy import Column , Integer, String,Boolean,ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column
from typing import List

# class Item(Base):
#     __tablename__ = 'items'
#     id:Mapped[int]=mapped_column(primary_key=True,index=True)
#     name:Mapped[str]
#     price:Mapped[int]
#     available:Mapped[bool]=mapped_column(default=True)
#     image_url:Mapped[str]
#     category_id:Mapped[int]=mapped_column(ForeignKey('categories.id'))
#     options: Mapped[List["Option"]] = relationship(
#         back_populates="item", cascade="all, delete-orphan"
#     )
#     category:Mapped["Category"]=relationship(back_populates="items")
#
#
# class Option(Base):
#     __tablename__ = 'options'
#     id:Mapped[int]=mapped_column(primary_key=True,index=True,)
#     name:Mapped[int]
#     price:Mapped[int]
#     item_id:Mapped[int]=mapped_column(ForeignKey('items.id'))
#     item:Mapped["Item"]=relationship(back_populates="options")
#
# class Category(Base):
#     __tablename__ = 'categories'
#     id:Mapped[int]=mapped_column(primary_key=True,index=True)
#     name:Mapped[str]
#     items:Mapped[List["Item"]]=relationship( back_populates="category",cascade="all, delete-orphan")
#
# class User(Base):
#     __tablename__ = 'users'
#     id:Mapped[int]=mapped_column(primary_key=True,index=True)
#     email:Mapped[str]=mapped_column(unique=True)
#     role:Mapped[str]
#     password:Mapped[str]

class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    price: Mapped[int]
    available: Mapped[bool] = mapped_column(default=True)
    image_url: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    options: Mapped[List["Option"]] = relationship(
        back_populates="item", cascade="all, delete-orphan"
    )
    category: Mapped["Category"] = relationship(back_populates="items")


class Option(Base):
    __tablename__ = 'options'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    price: Mapped[int]
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'),)
    item: Mapped["Item"] = relationship(back_populates="options",)

class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    items: Mapped[List["Item"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str]
    password: Mapped[str]