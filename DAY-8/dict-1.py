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

# delete 
_dict.pop('name')

del _dict['ram']

_dict.popitem()
_dict.popitem()
print(_dict)


# add
_dict['name'] = "Lenovo"

# update
_dict['name'] = "Hp"

# check
isThere = 'name' in _dict
print(isThere)

# copy
newDict = _dict.copy()

(1,)*3

# 3
# (1,1,1)

# nested dict
product = {
    'p1':{
        "name":"Dell",
        "price":1000
    },
    'p2':{
        "name":"HP",
        "price":2000
    }
}

product['p2']['price']