from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel, Field
# Создаем экземпляр приложения FastAPI
app = FastAPI()
# Определение базового маршрута

users =  []
class User(BaseModel):
    id: int
    username: str = Field(max_length=20, min_length=5,  description="Enter username")
    age : int = Field(ge=18, le=120, description="Enter age")

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
async def users(user: User):
    user_id = max((t.id for t in users), default=0) + 1
    users.append(User(id=user_id, username=user.username, age=user.age))
    return f'User {user_id} is registered'

@app.put ('/user/{user_id}/{username}/{age}')
async def update_task(user_id:int, user:User):
    try:
        for i in users:
            if i.id == user_id:
                i.username = user.username
                i.age = user.age
                return f'The user {user_id}  is updated '
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def users(user_id:int):
    try:
        for i, t in enumerate(users):
            if t.id == user_id:
                y = users[i]
                del users[i]
                return y
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
