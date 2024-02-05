'''
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
'''

from datetime import datetime
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field


    
class User(BaseModel):
    user_id:int=Field(...,title="User id")
    first_name: str=Field(...,title="First Name", max_length=20)
    second_name: str=Field(title="Second Name", max_length=20)
    email:str=Field(...,title="email", max_length=128)
    password:str=Field(...,title="Password",max_length=128)
    
class UserIn(BaseModel):
    first_name: str=Field(...,title="First Name", max_length=20)
    second_name: str=Field(title="Second Name", max_length=20)
    email:str=Field(...,title="email", max_length=128)
    password:str=Field(...,title="Password",max_length=128)
    
    
class Product(BaseModel):
    product_id: int=Field(...,title="Product id")
    product_name:str = Field(title="Product Name", max_length=20)
    description: str = Field(default=None, title="Product Description",max_length=1000)
    price: float = Field(...,title="Product Price", gt=0, le=100000)

class ProductIn(BaseModel):
    
    product_name:str = Field(title="Product Name", max_length=20)
    description: str = Field(default=None, title="Product Description",max_length=1000)
    price: float = Field(...,title="Product Price", gt=0, le=100000)
    
class Order(BaseModel):
    order_id:int=Field(...,title="Order id")
    user_id:int=Field(...,title="User id")
    product_id: int=Field(...,title="Product id")
    status:str=Field(...,title="Status",max_length=20)
    date_: datetime = Field(default_factory=datetime.now, title="Date")
    
class OrderIn(BaseModel):
    
    user_id:int=Field(...,title="User id")
    product_id: int=Field(...,title="Product id")
    date_: datetime = Field(default_factory=datetime.now, title="Date")
    status:str=Field(...,title="Status",max_length=20) 