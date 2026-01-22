from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Full CRUD API", version="1.0.0")

# === USERS ===
users_db: List[User] = []

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class User(UserCreate):
    id: int
    created_at: datetime

# === ITEMS ===
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# === TODOS ===
todos: List[Todo] = []
class Todo(BaseModel):
    id: int
    text: str
    completed: bool = False

# === ROUTES ===
@app.get("/")
def read_root():
    return {"message": "Full CRUD API работает!"}

# USERS CRUD
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    new_user = User(id=len(users_db) + 1, **user.dict(), created_at=datetime.now())
    users_db.append(new_user)
    return new_user

@app.get("/users", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id: return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            users_db[i] = User(id=user_id, **user.dict(), created_at=u.created_at)
            return users_db[i]
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# ITEMS
@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# TODOS
@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return todo

@app.get("/todos")
def get_todos() -> List[Todo]:
    return todos

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
