a = 10
b = 0

# print(a/b)

# c = int(input("Enter a number"))

l = [10,20,30]

# print(l[5])

d = {
    "name":"Deepak"
}

print(d["age"])


# ZeroDivisionError => When a denominator is zero.
# ValueError => when a invalid value is passed.
# IndexError => If a given list doesn't consist that index.
# KeyError => So when a dictionary doesn't have provided key.
# NameError => The given variable is not available.
# FileNotFoundError => if the given file name does not exist.
# TypeError => When a wrong data type is provided.

try:
    pass
    # risk code
except exceptionName:
    # response code
    pass
else:
    # If risk code is passed, then else will run.
    pass
finally:
    #It runs with every situation.
    pass