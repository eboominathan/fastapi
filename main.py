from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from typing import List 
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=str(uuid4()),
        first_name="Boomi",
        last_name="Nathan",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=str(uuid4()),
        first_name="Akshaya",
        last_name="Kavin",
        gender=Gender.male,
        roles=[Role.student]
    )
]

@app.get("/api/users")
def users():
    return db

@app.post("/api/users")
def createUser(user: User):
    user.id = str(uuid4())  # Generate new UUID for the user
    db.append(user)
    return {"id": user.id}

@app.put("/api/users/{user_id}")
def updateUser(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")

@app.delete("/api/users/{user_id}")
def deleteUser(user_id:UUID):
        for user in db:
           if user.id == user_id:
                db.remove(user)
                return {"msg":"Deleted"}
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exist")