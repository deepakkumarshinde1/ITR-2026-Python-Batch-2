string1 = "deepak"
string2 = 'deepak'
string3 = """deepak"""
string4 = '''deepak'''

text = "india is My country"

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

text2 = "    india is My country.  "
# print(len(text2))
# print(text2)
text3 = text2.strip()
# print(text3)
# print(len(text3))


text = "india is My country"
# print(text.replace('india','bharat'))

print(text.find('is'))
print(text.count('in'))
print(text.startswith("b"))
print(text.endswith("catch"))

# string => array
# array i.e list
text = "20-06-1991"
text_list = text.split("-")
newText = "/".join(text_list)
print(text_list)
print(newText)

a = 10
b = 20
c = a+b
print(f"The addition of given number i.e {a} + {b} = {c}")