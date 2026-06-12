_list = []
while True:
    number = input("Enter number or done = ")
    if(number == "done"):
        break
    _list.append(int(number))

if len(_list) > 0:
    max = _list[0]
    min = _list[0]
    for value in _list:
        if max < value:
            max = value
        if min > value:
            min = value
    print(f"The max number from list is = {max}")    
    print(f"The min number from list is = {min}")    
else:
    print("list in empty")


# Enter number or done = 5
# Enter number or done = 4
# Enter number or done = 7
# Enter number or done = 3
# Enter number or done = 2
# Enter number or done = done
# The max number from list is = 7
# The min number from list is = 2