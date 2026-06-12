
tableNumber = int(input("Enter a table number = "))

print(f"The table for {tableNumber} is")

for i in range(1,11):
    print(f"{i} x {tableNumber} = {tableNumber*i}")