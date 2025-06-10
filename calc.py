# write a basic calculator with functions add, subtract, multiply and divide (also check divide by zero)
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Divide by zero")
    else:
        return a / b
