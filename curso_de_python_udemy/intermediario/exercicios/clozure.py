# is a function that remembers the values of variables from its enclosing scope, even after
# the enclosing scope has finished.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_function = outer_function(10)
result = closure_function(5)
print(result)

#memoization(caching results):
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

#state machines(managing state):
def traffic_light():
    state = 'red'
    def next_state():
        nonlocal state
        if state == 'red':
            state = 'green'
        elif state == 'green':
            state = 'yellow'
        else:
            state = 'red'
        return state
    return next_state

light = traffic_light()
print(light())
print(light())

#event handling(handlig events):
def create_click_handler(button_text):
    def handler():
        print(f"button '{button_text}' clicked!")
    return handler

button1_click = create_click_handler("button 1")
button2_click = create_click_handler("button 2")

# Simulate button clicks
button1_click()
button2_click()