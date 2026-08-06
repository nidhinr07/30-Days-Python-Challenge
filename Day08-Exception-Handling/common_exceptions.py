# Day 08 - Common Python Exceptions

# -----------------------------------
# ValueError
# -----------------------------------

try:
    number = int(input("Enter a number: "))     # Enter integer

except ValueError:
    print("ValueError occurred.")


# -----------------------------------
# ZeroDivisionError
# -----------------------------------

try:
    print(10 / 0)                               # Divide by zero

except ZeroDivisionError:
    print("ZeroDivisionError occurred.")


# -----------------------------------
# NameError
# -----------------------------------

try:
    print(name)                                 # Undefined variable

except NameError:
    print("NameError occurred.")


# -----------------------------------
# TypeError
# -----------------------------------

try:
    result = "10" + 20                          # Different data types

except TypeError:
    print("TypeError occurred.")


# -----------------------------------
# IndexError
# -----------------------------------

numbers = [10, 20, 30]

try:
    print(numbers[5])                           # Invalid index

except IndexError:
    print("IndexError occurred.")


# -----------------------------------
# KeyError
# -----------------------------------

student = {
    "name": "Alex",
    "age": 20
}

try:
    print(student["course"])                    # Missing key

except KeyError:
    print("KeyError occurred.")


# -----------------------------------
# FileNotFoundError
# -----------------------------------

try:
    file = open("demo.txt", "r")                # File not found

except FileNotFoundError:
    print("FileNotFoundError occurred.")
