# Day 18 - Command Line Utility and Walrus Operator


# -----------------------------------
# Command Line Arguments
# -----------------------------------

import sys

print(sys.argv)                           # Display command line arguments

print("Program Name:", sys.argv[0])       # Display program file name


# -----------------------------------
# Accessing Arguments
# -----------------------------------

if len(sys.argv) > 1:

    name = sys.argv[1]                    # Get first command argument

    print("Hello", name)                  # Display given name


# -----------------------------------
# Walrus Operator
# -----------------------------------

if (number := 10) > 5:

    print(number)                         # Display assigned number


# -----------------------------------
# Walrus With Input
# -----------------------------------

while (value := input("Enter value: ")) != "exit":

    print("You entered:", value)          # Display entered value
