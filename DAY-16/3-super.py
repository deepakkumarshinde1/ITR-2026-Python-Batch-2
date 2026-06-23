# super is keyword and can call 
# parent's prop & func in child class
# calling parent constructor with super
class Person:
    def __init__(self,name):
        self.name = name
    
    def introduction(self):
        print(f"My Name is {self.name}")

class Student(Person):

    def __init__(self,name,course):
        super().__init__(name) # this will cal parent constructor
        self.course = course 

    def introduction(self):
        super().introduction()
        print(f"I am studding {self.course}")

student = Student("Rupali","Python AI/ML")
student.introduction()


student1 = Student("Deepak","Java Full Stack")
student1.introduction()