from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")
