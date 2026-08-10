# Day 12 - map(), filter() and reduce()

from functools import reduce


# -----------------------------------
# map() Function
# -----------------------------------

numbers = [1, 2, 3, 4, 5]                  # Create number list

squares = list(map(lambda x: x * x, numbers))

print(squares)                             # Display squared values


# -----------------------------------
# map() with Strings
# -----------------------------------

names = ["alex", "john", "david"]          # Create name list

upper_names = list(map(lambda name: name.upper(), names))

print(upper_names)                         # Display uppercase names


# -----------------------------------
# filter() Function
# -----------------------------------

numbers = [1, 2, 3, 4, 5, 6]               # Create number list

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)                        # Display even numbers


# -----------------------------------
# filter() with Condition
# -----------------------------------

ages = [12, 18, 21, 15, 25]                # Create age list

adults = list(
    filter(lambda age: age >= 18, ages)
)

print(adults)                              # Display adult ages


# -----------------------------------
# reduce() Function
# -----------------------------------

numbers = [1, 2, 3, 4, 5]                  # Create number list

total = reduce(lambda x, y: x + y, numbers)

print(total)                               # Display total


# -----------------------------------
# reduce() for Multiplication
# -----------------------------------

numbers = [1, 2, 3, 4, 5]                  # Create number list

product = reduce(lambda x, y: x * y, numbers)

print(product)                             # Display product
