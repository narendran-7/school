from mongoengine import connect, Document, StringField, IntField, DateTimeField
from datetime import datetime

connect("school")

class Student(Document):
    Roll_no = IntField(required=True)
    Name = StringField(required=True )
    Age = IntField(max_value=100)
    DOB = StringField(required=True, )
    Mail = StringField(required=True, )
    Dep = StringField(required=True, )
    Addr = StringField(required=True, )
    Ph_no = IntField()
    Date = DateTimeField(default=datetime.utcnow)