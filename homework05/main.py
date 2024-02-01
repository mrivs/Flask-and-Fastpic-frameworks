'''
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.



uvicorn main:app --reload
'''

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []

@app.on_event("startup")
async def startup_event():
    users.append(User(id=1, name="Vasya", email="vasya@mail.com", password="123"))
    users.append(User(id=2, name="Petya", email="petya@mail.com", password="456"))

@app.get("/")
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.put("/update_user/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            user.email = updated_user.email
            user.password = updated_user.password
            return {"message": "User updated successfully"}
    return {"error": "User not found"}

@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}

@app.get("/add_user/")
async def add_user_form(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request})


@app.post("/create_user/")
async def create_user(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    user_id = len(users) + 1
    new_user = User(id=user_id, name=name, email=email, password=password)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})
