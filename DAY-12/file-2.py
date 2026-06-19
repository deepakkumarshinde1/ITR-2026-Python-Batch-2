with open("student.txt","r") as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # data = file.readlines()
    # print(data)
    # print(file.tell())
    file.seek(3) # Moves the cursor to the given number location.
    print(file.read(3)) # 3 is Count of characters
    print(file.tell()) # Provides a cursor position.

# File exception handling.

try:
    file = open("hello.py","r")
    file.read()  
except FileNotFoundError:
    print("file not found")