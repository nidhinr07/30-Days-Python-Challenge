# Day 06 - Lists and Tuples

# -------------------------------
# Lists
# -------------------------------

fruits = ["Apple", "Banana", "Orange"]     # Create a list

print(fruits)                              # Display list


# -------------------------------
# Accessing List Elements
# -------------------------------

print(fruits[0])                           # First element
print(fruits[1])                           # Second element
print(fruits[-1])                          # Last element


# -------------------------------
# List Slicing
# -------------------------------

numbers = [10, 20, 30, 40, 50]             # Create number list

print(numbers[1:4])                        # Slice list
print(numbers[:3])                         # First three items
print(numbers[2:])                         # From index 2


# -------------------------------
# Updating List
# -------------------------------

fruits[1] = "Mango"                        # Update element

print(fruits)                              # Display updated list


# -------------------------------
# List Methods
# -------------------------------

numbers = [10, 20, 30, 40]                 # Create list

numbers.append(50)                         # Add one item
print(numbers)

numbers.extend([60, 70])                   # Add multiple items
print(numbers)

numbers.insert(2, 25)                      # Insert at index
print(numbers)

numbers.remove(30)                         # Remove item
print(numbers)

numbers.pop()                              # Remove last item
print(numbers)

numbers.sort()                             # Sort list
print(numbers)

numbers.reverse()                          # Reverse list
print(numbers)

print(numbers.count(20))                   # Count occurrences


# -------------------------------
# List Comprehension
# -------------------------------

square = [number ** 2 for number in range(1, 6)]   # Square numbers

print(square)


# -------------------------------
# Tuples
# -------------------------------

colors = ("Red", "Green", "Blue")          # Create tuple

print(colors)


# -------------------------------
# Accessing Tuple Elements
# -------------------------------

print(colors[0])                           # First element
print(colors[-1])                          # Last element


# -------------------------------
# Tuple Methods
# -------------------------------

marks = (90, 80, 90, 70, 60)               # Create tuple

print(marks.count(90))                     # Count value

print(marks.index(70))                     # Find index


# -------------------------------
# Packing and Unpacking
# -------------------------------

student = ("Alex", 20, "Python")           # Tuple packing

name, age, course = student                # Tuple unpacking

print(name)
print(age)
print(course)
