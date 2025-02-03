from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)

result = double(5)
print(result)

def greet(greeting, name):
    print(f"{greeting}, {name}!")

hello_greeter = partial(greet, "hello")

hello_greeter("alice")