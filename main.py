from fastapi import FastAPI, status, HTTPException

from models import Student

from schemas import StudentInfo, StudentUpdate

from json import loads

app = FastAPI()

@app.get("/all")
def all():
    return loads(Student.objects.all().to_json())

@app.post("/create_user")
def create_user(stud_info: StudentInfo):
    if Student.objects(Mail = stud_info.Mail):
        return {"message": f"User {stud_info.Mail} already exist"}
    else:
        Student(
            Roll_no = stud_info.Roll_no,
            Name = stud_info.Name,
            Age = stud_info.Age,
            DOB = stud_info.DOB,
            Mail = stud_info.Mail,
            Dep = stud_info.Dep,
            Addr = stud_info.Addr,
            Ph_no = stud_info.Ph_no,
        ).save()
        return {"message": f"Student {stud_info.Name} create successfully"}


@app.get("/get_user/{mail}")
def get_user(mail: str):
    if Student.objects(Mail = mail):
        return loads(Student.objects(Mail = mail).to_json())
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found!")

@app.delete("/delete_user/{mail}")
def delete_user(mail: str):
    if Student.objects(Mail = mail):
        Student.objects(Mail = mail).delete()
        return {"message": f"Student {mail} delete successfully"}
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found!")

@app.patch("/update_user/{mail}")
def update_user(mail, update_student: StudentUpdate):
    student = Student.objects(Mail = mail)
    if student:
        student.update(**update_student.dict(exclude_unset=True))
        return {"message": "Student updated successfully"}
    else:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No user found!")



