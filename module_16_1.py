from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def private() -> dict:
    return {"message": f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: int):
    return (f"Вы вошли как пользователь № {user_id}")


@app.get("/user")
async def info_user(first_name: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {first_name}, Возраст: {age}"}
