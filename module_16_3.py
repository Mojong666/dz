from fastapi import FastAPI, Path
# from typing import Annotated

app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def users_all(users: str) -> dict:
    return users_db
@app.post("/user/{username}/{age}")
async def user_info(username: str, age: int) -> str:
    current_index = str(int(max(users_db, key=int))+1)
    users_db[current_index] = username, age
    return "User <user_id> is registered"
@app.put("/user/{user_id}/{username}/{age}")
async def user_change(user_id: int, username: str, age: int) -> str:
    users_db[user_id] = username, age
    return "The user <user_id> is registered"
@app.delete("/user/{user_id}")
async def user_del(user_id: str) -> str:
    users_db.pop(user_id)
    return f"Message with {user_id} was deleted."
