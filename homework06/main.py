'''
Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.

• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

'''

import datetime
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy

from pyd_models import User,UserIn,Product,ProductIn,Order,OrderIn

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table("users",metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(20)),
    sqlalchemy.Column("second_name", sqlalchemy.String(20)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128))
)

products = sqlalchemy.Table("products",metadata,
    sqlalchemy.Column("product_id", sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("product_name", sqlalchemy.String(20)),
    sqlalchemy.Column("description", sqlalchemy.String(1000)),
    sqlalchemy.Column("price", sqlalchemy.Float)
)
    

orders = sqlalchemy.Table("orders",metadata,
    sqlalchemy.Column("order_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.user_id')),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.product_id')),
    sqlalchemy.Column("date_", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String(20))
)


engine = sqlalchemy.create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
metadata.create_all(engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(first_name=f'user{i}',second_name=f'Smit{i}',email=f'mail{i}@mail.ru',password="admin")
        await database.execute(query)
    return {'message': f'{count} fake users create'}

@app.get("/fake_products/{count}")
async def create_note(count: int):
    for i in range(count):
        query = products.insert().values(product_name=f'product{i}',description=f'product{i}',price=i*100)
        await database.execute(query)
    return {'message': f'{count} fake users create'}

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    '''Создание пользователя в БД, create '''
    query = users.insert().values(first_name=user.first_name,second_name=user.second_name,
    email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    # print(last_record_id)
    return {**user.dict(), "user_id": last_record_id}

@app.get("/users/", response_model=List[User])
async def read_users():
    ''' Чтение пользователей из БД, read'''
    query = users.select()
    return await database.fetch_all(query)

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    '''Чтение одного пользователя из БД, read'''
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    '''Обновление пользователя в БД, update '''
    query = users.update().where(users.c.user_id ==user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "user_id": user_id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    '''Удаление пользователя из БД, delete'''
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    '''Создание order в БД, create '''
    query = orders.insert().values(user_id=order.user_id,product_id=order.product_id,date_=order.date_,status=order.status)
    last_record_id = await database.execute(query)
    # print(last_record_id)
    return {**order.dict(), "order_id": last_record_id}

@app.get("/orders/", response_model=List[Order])
async def read_orders():
    ''' Чтение orders из БД, read'''
    query = orders.select()
    return await database.fetch_all(query)

@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    '''Чтение одного order из БД, read'''
    query = orders.select().where(orders.c.order_id == order_id)
    return await database.fetch_one(query)

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    '''Обновление order в БД, update '''
    query = orders.update().where(orders.c.order_id ==order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "order_id": order_id}

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    '''Удаление order из БД, delete'''
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {'message': 'order deleted'}


@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    '''Создание product в БД, create '''
    query = orders.insert().values(product_name=product.product_name,description=product.description,price=product.price)
    last_record_id = await database.execute(query)
    # print(last_record_id)
    return {**product.dict(), "product_id": last_record_id}

@app.get("/products/", response_model=List[Product])
async def read_products():
    ''' Чтение products из БД, read'''
    query = orders.select()
    return await database.fetch_all(query)

@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    '''Чтение одного product из БД, read'''
    query = orders.select().where(products.c.product_id == product_id)
    return await database.fetch_one(query)

@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    '''Обновление product в БД, update '''
    query = products.update().where(products.c.product_id ==product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "product_id": product_id}

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    '''Удаление product из БД, delete'''
    query = products.delete().where(products.c.product_id == product_id)
    await database.execute(query)
    return {'message': 'product deleted'}