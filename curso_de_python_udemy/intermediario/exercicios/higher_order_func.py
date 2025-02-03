#take other functions as arguments or return functions as results.

#Map:
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers)) 
# Output: [1, 4, 9, 16, 25]

#Filter:
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))
# Output: [2, 4]

#Reduce:
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)
# Output: 15

#lambda functions:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]

#custom higher-order functions:
def apply_to_each(func, iterable):
    return [func(item) for item in iterable]

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_each(lambda x: x**2, numbers)
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

#chaining functions:
def add_one(x):
    return x + 1

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result = list(map(square, map(add_one, numbers)))
print(result)
# Output: [4, 9, 16, 25, 36]

#partial aplication
from functools import partial
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))
# Output: 10
print(triple(4))
# Output: 12

#caching results:
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))