from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута

users =  {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def root():
    return "Главная страница"

@app.get("/user/admin")
async def read_item():
    return "Вы вошли как администратор"

@app.get('/users')
async def users():
    return users

@app.post('/user/{username}/{age}')
async def users(username: Annotated[str, Path(min_length=5, max_length=20,  description="Enter username", example="Erturyn")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="20")]):
    user_id = max(users.keys()) + 1
    new_task = {user_id, f"Имя: {username}, возраст: {age}"}
    users.append(new_task)
    return f'User {user_id} is registered'

@app.put ('/user/{user_id}/{username}/{age}')
async def update_task(user_id:int,username: Annotated[str, Path(min_length=5, max_length=20,  description="Enter username", example="Erturyn")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="20")]):
        users[f'{user_id}'] = f"Имя: {username}, возраст: {age}"
        return f'The user {user_id}  is updated '

@app.delete('/user/{user_id}')
async def users(user_id:int):
    users.pop(f"{user_id}")
