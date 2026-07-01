import json

# JSON is nothing but it's a JavaScript object notation.
# It's a independent language which is basically used for interchange data in between two parties.
# So in Python, JSON looks like a dictionary only.

student = {
    "name":"deepak",
    "age":36
}

# dictionary to json string  => dumps
print(student)
print(type(student))
json_data = json.dumps(student) # JSON formatted string.
print(json_data) 
print(type(json_data)) # string (Preserved)


# json string to dictionary => loads
string_json = '''{
    "id": 1,
    "name": "Rohit",
    "email": "Sincere@april.biz",
    "website": "hildegard.org"
  }'''

student_data = json.loads(string_json) #

print(student_data['name'], type(student_data))


# dump => write a json file ( add data )
# load => read a json file ( read )

with open('data.json','w') as file:
    json.dump(student,file,indent=4)   # write a data in json file


with open('data.json','r') as file:
    data = json.load(file)   # read data & converts to str json 
    print(data)
