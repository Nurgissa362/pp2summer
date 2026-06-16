def my_function():
    return None
print("Using __doc__:")
print(my_function.__doc__)
print("Using help():")
help(my_function)


def greet(name):
    return f"Hello, {name}!"


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed.")
    return a / b
print(divide(6, 2))
print(multiply(3, 5))