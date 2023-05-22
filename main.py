from fastapi import FastAPI

# DB model
from models import Student

# Request body schema
from schemas import StudentInfo


app = FastAPI()

@app.get("/")
def index():
    return {"message":"hello"}

@app.post("/create_user")
def create_user(stud_info: StudentInfo):
    Student(
        Roll_no = stud_info.Roll_no,
        Name = stud_info.Name,
        Age = stud_info.Age,
        DOB = stud_info.DOB,
        Dep = stud_info.Dep,
        Addr = stud_info.Addr,
        Ph_no = stud_info.Ph_no,
    ).save()
    return {"message": f"Student {stud_info.Name} create successfully"}
