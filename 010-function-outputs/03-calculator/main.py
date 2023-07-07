from art import logo
from os import name, system


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Can't divide by zero"
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculation():
    print(logo)
    num1 = float(input("What's the first number? "))
    for k, operation in operations.items():
        print(k)

    should_calculate = True

    while should_calculate:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        operation = operations.get(operation_symbol)
        answer = operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_calculate = False
            clear()


calculation()
