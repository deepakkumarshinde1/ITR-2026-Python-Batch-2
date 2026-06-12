# parameter
def printName(name):
    print("Hello ",name)

printName("Madhur")
printName("Soham")
printName("Dipali")

# multiple arg 
# b as default value
def add(a,b=0):
    print(a+b)

add(10,20)
add(10)



def userDetails(name,lastName):
    print(f"hi, {name} {lastName}")

# keyword arguments
userDetails(lastName="shinde",name="deepak")


# variable length arguments
def numbers(*a):
    print(a)

numbers(1,2,3,4)

# keyword variable length arguments

def floatNumber(**a):
    print(a)

floatNumber(a=10.5,b=2.5,c=3.5,d=4.0)



