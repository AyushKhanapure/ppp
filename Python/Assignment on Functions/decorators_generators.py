def add_greeting(func):
    def wrapper(*args, **kwargs):
        print("Hey!")
        return func(*args, **kwargs)
    return wrapper

@add_greeting
def say_hello(name):
    return f"Hello, {name}!"

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_sequence()

print(say_hello("Rahul"))

print("Fibonacci sequence:")
for _ in range(10):
    print(next(fib_gen), end=" ")
