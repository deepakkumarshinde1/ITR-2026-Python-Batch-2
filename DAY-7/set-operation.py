# Union.
s1 = {1,2,3}
s2 = {1,2,4}

print(s1.union(s2))
print(s1 | s2) # {1, 2, 3, 4}

# intersection.
print(s1.intersection(s2)) # {1, 2}

# Difference
print(s1 - s2) # {3}

# Symmetric difference.
print(s1 ^ s2) # {3, 4}

s3 = s1.copy() # new copy
# add
# remove
# update
# discard
# pop
# clear
# union
# intersection
# Difference
# Symmetric difference
# copy

s4 = frozenset([1,2,3,4])
print(s4)

setList = list(s1)
setOne = set(setList)
print(setOne)


# []  () {}
# m   im  m
# d   d   no-dup
# mo  ls mo
# ix. ix  no   