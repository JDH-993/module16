from fastapi import FastAPI
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута
@app.get("/")
async def welc():
    return "Главная страница"

@app.get("/user/admin")
async def read_item():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def polz(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def read_item(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
