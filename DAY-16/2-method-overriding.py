# method overloading
class Person:
    def introduction(self):
        print("My Name is deepak")

class Student(Person):
    def introduction(self):
        print("I am studding python for DS")

student = Student()
student.introduction()

