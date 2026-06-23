class Teacher:
    name = "deepak" # public
    _age = 36 # protected
    __salary = 20000 #private

    def getSalaryDetails(self):
        print(self.__salary)

t = Teacher()
print(t.name)
print(t._age)
t.getSalaryDetails()