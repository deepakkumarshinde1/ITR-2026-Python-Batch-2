class Student:
    name = ""
    def __init__(self,age):
        self.age = age

    def print(self,name):
        self.name = name
        


student = Student(30)
student.print("Rohini")