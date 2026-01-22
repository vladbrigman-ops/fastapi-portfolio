from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Users API", version="1.0.0")

# In-memory database (для фриланса хватит)
users_db: List = []

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class User(UserCreate):
    id: int
    created_at: datetime

# CREATE
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    new_user = User(
        id=len(users_db) + 1,
        name=user.name,
        email=user.email,
        age=user.age,
        created_at=datetime.now()
    )
    users_db.append(new_user)
    return new_user

# READ all
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

# READ one
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            users_db[i] = User(id=user_id, **user.dict(), created_at=u.created_at)
            return users_db[i]
    raise HTTPException(status_code=404, detail="User not found")

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
@app.post("/items/")
def create_item(item: Item):  # Pydantic модель
    return item

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Влад"}
import os
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
