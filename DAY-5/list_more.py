productList = ["Dell","Lenovo","HP","Lenovo"]
productList2 = ["A","B","C"]
# last
# productList.append("Apple")

# at a location ( index )
# productList.insert(2,"Apple")

# Merge a list.
productList.extend(productList2)
# print(productList)

# remove
# productList.remove("Lenovo")
# productList.pop(1)
# productList.pop()
# productList.pop()
# productList.clear()


newValue = "D" 
check = newValue in productList

if(check == False):
    productList.append(newValue)
# print(productList)


for index,name in enumerate(productList):
    # print(index,name)
    pass

p1List = [1,5,3,7,5,2,3,11]
p2List = [10,20,30,40,50,60]
p3List = p2List + p1List
# p1List.sort()
p1List.reverse()
# print(p1List)



studentName = ["deepak","ram","manoj"]
students = studentName.copy()
studentName3 = studentName*3 
# print(studentName3)

# index
numbers = [10,20,30,40,30,60,30]
# print(numbers.index(300))
# count
# print(numbers.count(300))


# append
# insert
# extend
# remove
# pop
# clear
# reverse
# [] + []
# sort
# copy
# index
# count

