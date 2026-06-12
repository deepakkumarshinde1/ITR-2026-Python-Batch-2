# input
n1 = int(input("Enter a starting number = "))
n2 = int(input("Enter a end number = "))
_list = []
for value in range(n1,n2+1):
    if value % 2 == 0:
        _list.append(value)

print(_list)


# Enter a starting number = 3
# Enter a end number = 17
# [4, 6, 8, 10, 12, 14, 16]