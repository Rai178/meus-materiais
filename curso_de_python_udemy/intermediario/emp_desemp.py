# #unpacking a tuple
# point = (3, 4)
# x, y = point
# print(x) # output: 3
# print(y) # output: 4 

# numbers = [1, 2, 3]
# a, b, c = numbers
# print(a) # output: 1
# print(b) # output: 2
# print(c) # output: 3


# string = "AB"
# first, second = string
# print(first) 
# print(second)

# numbers = [1, 2, 3, 4, 5]
# a, *rest = numbers
# print(a)
# print(rest)

# *start, last = numbers
# print(start)
# print(last)

# # packing values into a tuple
# packed = 1, 2, 3
# print(packed)

# # packing values into a list
# packed_list = [4, 5, 6]
# print(packed_list)

# def add(x, y, z):
#     return x + y + z

# nums = [1, 2, 3]
# result = add(*nums) 
# print(result)

# def display_info(name, age):
#     print(f"name: {name}, age: {age}")

# info = {'name': 'alice', 'age': 25}
# display_info(**info) # unpacks the dictionary into keyword arguments

def add(x, y, z):
    return x + y + z

# using * to unpack a list or tuple
nums = [1, 2, 3]
result = add(*nums) # unpacks nums to pass 1, 2, 3 as x, y, z
print(result)

coords = (10, 20, 30)
print(add(*coords))

def display_info(name, age):
    print(f"name: {name}, age: {age}")

# unpacking a dictionary into function arguments
person = {"name": "alice", "age": 30}
display_info(**person) # unpacks the dictionary into name='alice', age=30
# output: name: alice, age: 30