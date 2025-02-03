#map(function, iterable)

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)