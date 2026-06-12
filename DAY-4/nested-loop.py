
#nested loop
for i in range(5):
    for j in range(3):
        print(f"this is a inner loop running for {i} time  with j as {j}")

# example of table
tableRange = 10
for i in range(1,tableRange+1):
    print(f"\nBellow is table {i}")
    for j in range(1,11):
     print(f"{j} x {i} = {j*i}")

# example of table by user choice
startTableRange = int(input("Enter a start table number = "))
endTableRange = int(input("Enter a end table number = "))
for i in range(startTableRange,endTableRange+1):
    print(f"\nBellow is table {i}")
    for j in range(1,11):
     print(f"{j} x {i} = {j*i}")