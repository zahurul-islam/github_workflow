# write a basic calculator with functions add, substruct, multipy and devide (also check devide by zero)
def add(a, b):
    return a + b


def substruct(a, b):
    return a - b


def multipy(a, b):
    return a * b


def devide(a, b):
    if b == 0:
        return "Error: Devide by zero"
    else:
        return a / b

