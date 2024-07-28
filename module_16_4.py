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
