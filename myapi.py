from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Purity",
        "age": 21,
        "career": "Computer Science",
    }
}
class Student(BaseModel):
     name: str
     age: int
     year: str
     
class UpdateStudent(BaseModel):
     name: Optional[str] = None
     age: Optional[int] = None
     year: Optional[str] = None
     
@app.get("/")
def index():
    return {"message": "Welcome"}

@app.get("/student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", ge=0)):
    if student_id in students:
        return students[student_id]
    else:
        return {"error": "Student not found"}

@app.get("/get-by-name")
def get_student(name: Optional [str]):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
        return {"error": "Student not found"}
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    if student_id in students:
        return {"error" : "Student already exists"} 
    
    students[student_id] = student.dict()
    return students[student_id]

@app.post("/update-student/{studentid}")
def update_student(student_id: int, student: UpdateStudent ):
    if student_id not in  students:
        return {"error": "Student not found"}
    if student.name is not None:
        students[student_id]['name'] = student.name
        
    if student.age is not None:
        students[student_id]['age'] = student.name
        
    if student.year is not None:
        students[student_id]['year'] = student.name

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def detelet_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}