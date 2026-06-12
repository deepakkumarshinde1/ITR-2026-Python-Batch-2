# value = lambda param: logic

# def add(a,b):
#     return a+b
# result = add(10,20)


# def add(a,b):
#     return a+b
result = lambda a,b:a+b
# return a plus b

print(result(10,30))
# def evenOdd(n):
#     if n%2 == 0:
#         return "event"
#     else:
#         return "odd"
    
# result = evenOdd(10)

result = lambda n: "even" if n%2==0  else "odd" 
# return even if n%2 is equals 0 else return odd
print(result(10))
print(result(11))