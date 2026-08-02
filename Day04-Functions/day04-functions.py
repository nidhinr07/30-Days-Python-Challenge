# Day 04 - Functions

# Built-in function examples
language = "Python"                 # Store string

print(len(language))                # Find string length
print(type(language))               # Display data type


# User-defined function
def greet():
    print("Welcome to Python")      # Display greeting

greet()                             # Call function


# Function with arguments
def add(num1, num2):
    print(num1 + num2)              # Display sum

add(10, 20)                         # Pass values


# Positional arguments
def introduce(name, course):
    print(name)                     # Display name
    print(course)                   # Display course

introduce("Alex", "Python")         # Position matters


# Keyword arguments
def student(name, course):
    print(name)                     # Display name
    print(course)                   # Display course

student(course="Python", name="Alex")  # Order does not matter


# Variable-length arguments
def numbers(*values):
    print(values)                   # Display tuple

numbers(10, 20, 30, 40)             # Multiple arguments


# Return statement
def square(number):
    return number * number          # Return square

result = square(5)                  # Store returned value

print(result)                       # Display result
