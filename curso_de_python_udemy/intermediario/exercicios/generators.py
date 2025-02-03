# Generator expressions: a concise way to create iterators
# (expression for item in iterable)

squares = (x**2 for x in range(10))
print(squares) # Output: <generator object <genexpr> at 0x7f8a23456789>

for square in squares:
    print(square)

#filtering:
even_numbers = (x for x in range(10) if x % 2 == 0)

#mapping:
squares = (x**2 for x in range(10))

#combining filtering and mapping:
even_squares = (x**2 for x in range(10) if x % 2 == 0)

# infinite iterators:
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i)

#data pipelines:
def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
def square(numbers):
    for num in numbers:
        yield num**2

numbers = range(10)
even_squares = (x**2 for x in filter_even(square(numbers)))

#lazy evaluation:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen))

#creating custom iterators:
def custom_iterator(start, end, step):
    for i in range(start, end, step):
        yield i

for num in custom_iterator(1, 10, 2):
    print(num)

#reading large files ifficiently:
def read_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

for line in read_large_file('large_file.txt'):
    # process each line
    print(line)