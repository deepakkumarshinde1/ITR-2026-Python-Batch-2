# key = value

_list = ["dell",65000,"1kg","13th Gen","intel i7", "16 GB"]
_tuple = ("dell",65000,"1kg","13th Gen","intel i7", "16 GB")
_set = {"dell",65000,"1kg","13th Gen","intel i7", "16 GB"}
_dict = {
    'name': "dell",
    "price":65000,
    "weight":"1kg",
    "gen":"13th Gen",
    "processor":"intel i7",
    "ram": "16 GB",
    "memory":"16 GB"
}
_dict_1 = {}
_dict_2 = dict(name="deepak",age="36")

# read
print(_dict['name'])
print(_dict.get('loc'))

for key in _dict:
    print("key =",key)

for value in _dict.values():
    print("value = ",value)

for key,value in _dict.items():
    print(key,'  = ',value)

# delete 
_dict.pop('')