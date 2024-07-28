# from fastapi import FastAPI, status, Body, HTTPException
# from pydantic import BaseModel
# from typing import List
#
# app = FastAPI()
#
# users_db = []
#
#
# class User(BaseModel):
#     id: int = None
#     username: str
#     age: int
#
#
# @app.get("/users")
# async def users_all() -> list:
#     return users_db
#
#
# @app.post("/user/{username}/{age}")
# async def user_info(username: User, age: User) -> str:
#     username.id = len(users_db)
#     users_db.append(User)
#     return "User <user_id> is registered"
#
#
# @app.put("/user/{user_id}/{username}/{age}")
# async def user_change(user_id: int, username: str, age: int) -> str:
#     users_db[user_id] = username, age
#     return "The user <user_id> is registered"
#
#
# @app.delete("/user/{user_id}")
# async def user_del(user_id: str) -> str:
#     users_db.pop(user_id)
#     return f"Message with {user_id} was deleted."
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Список users, будет использоваться для хранения пользователей
users = []

# Модель User
class User:
    def __init__(self, user_id: int, username: str, age: int):
        self.user_id = user_id
        self.username = username
        self.age = age

# GET запрос по маршруту '/users' возвращает список users
@app.get("/users")
def get_users():
    return users

# POST запрос по маршруту '/user/{username}/{age}' добавляет нового пользователя
@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    if users:
        new_id = users[-1].user_id + 1
    else:
        new_id = 1
    new_user = User(user_id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос по маршруту '/user/{user_id}/{username}/{age}' обновляет данные пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.user_id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос по маршруту '/user/{user_id}' удаляет пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")