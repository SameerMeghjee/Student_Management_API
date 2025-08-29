from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

# Create FastAPI instance
app = FastAPI()

# Student model
class Student(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr

# Default student list
students: List[Student] = [
    Student(name="Ali Khan", age=20, gender="Male", email="ali.khan@gmail.com"),
    Student(name="Sara Ahmed", age=22, gender="Female", email="sara.ahmed@gmail.com"),
    Student(name="Bilal Hussain", age=19, gender="Male", email="bilal.hussain@gmail.com"),
]

# Get all students
@app.get("/students")
def get_students():
    return students

# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

# Add a student
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully", "student_id": len(students) - 1}

# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = updated_student
    return {"message": "Student updated successfully"}

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted successfully", "deleted_student": deleted_student}
