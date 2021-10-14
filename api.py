# uvicorn api:app --reload 

from fastapi import FastAPI, Path

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
def get_student(student_id: int = Path(None, description="Enter the students id that you want to view")):
    return students[student_id]

