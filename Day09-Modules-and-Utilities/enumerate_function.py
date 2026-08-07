# Day 09 - enumerate() Function

# -----------------------------------
# Basic enumerate()
# -----------------------------------

fruits = ["Apple", "Banana", "Orange"]     # Create list

for index, fruit in enumerate(fruits):

    print(index, fruit)


# -----------------------------------
# enumerate() with start value
# -----------------------------------

students = ["Alex", "John", "David"]       # Create list

for roll_no, student in enumerate(students, start=1):

    print(roll_no, student)


# -----------------------------------
# enumerate() with Tuple
# -----------------------------------

colors = ("Red", "Green", "Blue")          # Create tuple

for index, color in enumerate(colors):

    print(index, color)
