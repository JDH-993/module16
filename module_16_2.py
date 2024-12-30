from fastapi import FastAPI, Path
from typing import Annotated
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
async def polz(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="12")]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def read_item(username: Annotated[str, Path(min_length=5, max_length=20,  description="Enter username", example="Erturyn")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="20")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
