# Basic calculator functions:
# - add, subtract, multiply
# - divide (with zero division check)
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
