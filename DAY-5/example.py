_list = []

#loop
cont = True
while True:
    number = input("Enter a number")
    # list
    _list.append(number)
    t = input("Do you want to add a new number ? Y/N = ")
    if(t == "N"):
        break

#print
print("Here is your list...")
for value in _list:
    print(value)