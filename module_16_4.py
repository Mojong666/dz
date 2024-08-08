from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Модель User с наследованием от BaseModel
class User(BaseModel):
    user_id: int
    username: str
    age: int

# Список пользователей
users: List[User] = []

# GET запрос по маршруту '/users' возвращает список users
@app.get("/users", response_model=List[User])
def get_users():
    return users

# POST запрос по маршруту '/user' добавляет нового пользователя
@app.post("/user", response_model=User)
def create_user(username: str, age: int):
    new_id = users[-1].user_id + 1 if users else 1
    new_user = User(user_id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос по маршруту '/user/{user_id}' обновляет данные пользователя
@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.user_id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос по маршруту '/user/{user_id}' удаляет пользователя
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
