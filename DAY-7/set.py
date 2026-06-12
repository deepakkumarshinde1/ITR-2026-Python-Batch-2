# set
# it's a collection of data.
# data is basically immutable in nature.So, 
# data is mutable in nature.
# It has unique data.

set1 = {1,2,3,4,4,4,4,4,4}
set2 = set() # for empty set
# set1.add(111)
# set1.remove(4)
set1.update([5,6,7,8,2.5])

set1.discard(11)
# set1.clear() => set() empty set
set1.pop() # removes for 1st
set1.pop()
set1.pop()

isThere = 11 in set1 # true or false

print(set1)


