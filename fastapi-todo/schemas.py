from pydantic import BaseModel


class TodoItemCreate(BaseModel):
    title: str
    completed: bool = False