# class starts
class Staff:

    #Constructor
    def __init__(self,staffName,staffSubject):
        self.name = staffName
        self.subject = staffSubject
        # print("inner constructor")
    
    def printName(self):
        print(self.name,self.subject)
# class ends        

# object
staff = Staff("deepak","python")
staff.printName()

staff2 = Staff("amol","java")
staff2.printName()