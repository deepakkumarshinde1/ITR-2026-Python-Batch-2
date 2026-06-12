# [] => list
# () => tuple
# {} => set 
# {key:value} dictionary

role = ("Student","Admin","Teacher","Student")
roll_no = (1,2,3,4)

# print(role[0])

v1,v2,v3,v4 = role

# print(role.count("Student"))
# print(role.index("Student"))
# print(v1,v2,v3)


# print(role[0:2])
# role[0]="User" => error 'tuple' object does not support item assignment

for value in role:
    # print(value)
    pass

# conversion and data type.
char = ('a',)
print(type(char))

# tuple => list
charList = list(char)
print(charList)

# list => tuple
charTuple = tuple(charList)
print(charTuple)

# concatenation
t1 = (1,2,3,4)
t2 = (11,22,33,44)

t3 = t1 + t2
print(t3)

# nested tuple
students = (
    ('Deepak',21),
    ('Ankush',21),
    ('Sojwal',21),
    ('Manisha',21),
)


# Repetition
t4 = ('soham',) * 3
print(t4)