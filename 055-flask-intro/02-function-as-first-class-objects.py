def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first class objects, can be passed around as arguments.
def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)


result = calculate(add, 2, 3)
print(result)


# Nested functions

def outer_functions():
    print("outer function")

    def nested_function():
        print("inner function")

    nested_function()


outer_functions()


# Functions can be returned
def return_nested():
    print("return nested function")

    def returned_function():
        print("returned function")

    return returned_function


returned_f = return_nested()
returned_f()
