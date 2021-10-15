# uvicorn api:app --reload 
# 
from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "james",
        "age": 25,
        "major": "biology"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="Enter the students id that you want to view", gt=0,lt=3)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "not found"}



