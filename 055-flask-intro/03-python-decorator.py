import time


# Python decorator function
def delay_decorator(function):

    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()
say_greeting()
say_bye()