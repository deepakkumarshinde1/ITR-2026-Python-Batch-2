
def div():
    try:
        numberOne = int(input("Enter 1st Number = "))
        numberTwo = int(input("Enter 2nd Number = "))
        result = numberOne/numberTwo
        print(result)
    except ValueError:
        print("Invalid values passed")
    except ZeroDivisionError:
        print("The denominator is zero, which is not allowed.")


# Multi-exception handling. For similar messages.
def listAndDict():
    try:
        numbers = [1,2,3]
        student = {
            "name":"deepak"
        }
        print(numbers[1])
        print(student['age'])
    except (IndexError,KeyError):
        print("Index number is out of boundary.")


# Exception with else.
def withElse():
    try:
        numbers = [1,2,3]
        student = {
            "name":"deepak"
        }
        value = student['name']
    except (IndexError,KeyError):
        print("Index number is out of boundary.")
    else:
        print(value)

def exampleOfFinally():
    try:
        name = "Neha"
        print(name)
    except NameError:
        print("Variable is not declared.")
    finally:
        print("I am finally output")

  

# file handling
try:
    file = open("user.log",'r');
    print(file.read())
except FileNotFoundError:
    print("file not found")
finally:
    try:
        file.close()
        print("is successfully closed.")
    except:
        pass


# Exception capturing.
try:
    print(10/0)
except Exception as error:
    print(error)