# Day 07 - Sets and Set Methods

# -----------------------------------
# Creating a Set
# -----------------------------------

numbers = {10, 20, 30, 40}               # Create a set

print(numbers)                           # Display set


# -----------------------------------
# Duplicate Values
# -----------------------------------

duplicate_numbers = {10, 20, 20, 30, 40} # Duplicate values

print(duplicate_numbers)                 # Duplicates removed


# -----------------------------------
# Adding Elements
# -----------------------------------

numbers.add(50)                          # Add one item

print(numbers)


# -----------------------------------
# Adding Multiple Elements
# -----------------------------------

numbers.update([60, 70])                 # Add multiple items

print(numbers)


# -----------------------------------
# Removing Elements
# -----------------------------------

numbers.remove(20)                       # Remove item

print(numbers)


# -----------------------------------
# Discard Method
# -----------------------------------

numbers.discard(100)                     # No error if missing

print(numbers)


# -----------------------------------
# Pop Method
# -----------------------------------

removed_item = numbers.pop()             # Remove random item

print("Removed :", removed_item)
print(numbers)


# -----------------------------------
# Union Method
# -----------------------------------

set1 = {1, 2, 3}                         # First set
set2 = {3, 4, 5}                         # Second set

print(set1.union(set2))                  # Combine sets


# -----------------------------------
# Intersection Method
# -----------------------------------

print(set1.intersection(set2))           # Common values


# -----------------------------------
# Clear Method
# -----------------------------------

temp = {100, 200, 300}                   # Temporary set

temp.clear()                             # Remove all items

print(temp)
