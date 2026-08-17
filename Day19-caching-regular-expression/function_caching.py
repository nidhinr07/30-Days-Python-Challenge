# Day 19 - Function Caching

from functools import lru_cache


# -----------------------------------
# Basic Function Caching
# -----------------------------------

@lru_cache
def square(number):
    return number * number                # Return square of number


print(square(5))                          # Calculate square
print(square(5))                          # Use cached result

print(square(10))                         # Calculate another square
print(square(10))                         # Use cached result


# -----------------------------------
# Fibonacci with Caching
# -----------------------------------

@lru_cache
def fibonacci(number):

    if number <= 1:
        return number                     # Return base value

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))                      # Calculate Fibonacci value
