def add(a,b):
    # local variable
    result = a + b
    print(result)
    return result

# global
r1 = add(50,10)
# print(result) 

x = 100

def printData():
    global x 
    x = 10
    print(x)

printData()
print(x)