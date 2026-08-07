# Day 09 - Importing Modules

# -----------------------------------
# Import Entire Module
# -----------------------------------

import math                              # Import math module

print(math.sqrt(25))                     # Square root
print(math.factorial(5))                 # Factorial


# -----------------------------------
# Import Specific Function
# -----------------------------------

from math import sqrt                    # Import sqrt only

print(sqrt(49))


# -----------------------------------
# Import Multiple Functions
# -----------------------------------

from math import sqrt, factorial         # Import selected functions

print(sqrt(64))
print(factorial(6))


# -----------------------------------
# Import All Functions
# -----------------------------------

from math import *                       # Import all functions

print(pow(2, 5))
print(floor(8.9))
print(ceil(8.1))


# -----------------------------------
# Import Module with Alias
# -----------------------------------

import math as m                         # Import with alias

print(m.pi)
print(m.sqrt(81))


# -----------------------------------
# Display Module Functions
# -----------------------------------

import math                              # Import math module

print(dir(math))                         # Show all functions
