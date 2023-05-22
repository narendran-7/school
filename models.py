from mongoengine import connect, Document, StringField, IntField, DateField

connect("school")

class Student(Document):
    Roll_no = IntField()
    Name = StringField()
    Age = IntField()
    DOB = StringField()
    Dep = StringField()
    Addr = StringField()
    Ph_no = IntField()