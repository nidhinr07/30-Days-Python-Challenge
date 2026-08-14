# Day 16 - Python Decorators


# -----------------------------------
# Basic Decorator
# -----------------------------------

def decorator_function(func):

    def wrapper():
        print("Before function")          # Run before function
        func()                            # Call original function
        print("After function")           # Run after function

    return wrapper


@decorator_function
def say_hello():

    print("Hello Python")                 # Display message


say_hello()                               # Call decorated function


# -----------------------------------
# Decorator with Arguments
# -----------------------------------

def welcome_decorator(func):

    def wrapper(name):
        print("Welcome!")                 # Display welcome message
        func(name)                        # Call original function

    return wrapper


@welcome_decorator
def greet(name):

    print(f"Hello {name}")                 # Display user name


greet("Alex")                             # Call decorated function
