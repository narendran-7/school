from pydantic import BaseModel


class StudentInfo(BaseModel):
    Roll_no: int
    Name: str
    Age: int
    DOB: str
    Mail: str
    Dep: str
    Addr: str
    Ph_no: int

class StudentUpdate(BaseModel):
    Roll_no: int
    Name: str
    Age: int
    DOB: str
    Dep: str
    Addr: str
    Ph_no: int