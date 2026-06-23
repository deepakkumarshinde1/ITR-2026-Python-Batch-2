# 1-inheritance.py
class Parent:
    pass

class Child(Parent):
    pass

child = Child()

# example-1
# class Employee:
#     name = "ABC"
#     def printEmpName(self):
#         print(f"Employee Name is {self.name}")

# class Staff(Employee):
#     pass


# staff = Staff()
# staff.printEmpName()
# print(staff.name)




# multi level inheritance

# class Employee:
#     name = "ABC"
#     def printEmpName(self):
#         print(f"Employee Name is {self.name}")

# class Staff(Employee):
#     age = 30


# class Teacher(Staff):
#     pass

# teacher = Teacher()
# teacher.printEmpName()
# print(teacher.name)
# print(teacher.age)


# multiple inheritance

class Employee:
    name = "ABC"
    def printEmpName(self):
        print(f"Employee Name is {self.name}")

class Staff(Employee):
    age = 30

class Salary:
    def printSalary(self):
        print("This is emp salary")

class Teacher(Staff,Salary):
    pass

teacher = Teacher()
teacher.printEmpName()
teacher.printSalary()
print(teacher.name)
print(teacher.age)