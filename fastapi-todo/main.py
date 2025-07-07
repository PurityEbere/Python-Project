from fastapi import FastAPI, Depends
from models import Todo
from typing import List
from schemas import TodoItemCreate
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

app = FastAPI()


models.Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Todo API is running"}


@app.post("/todos/")
def create_todo(todo: TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}