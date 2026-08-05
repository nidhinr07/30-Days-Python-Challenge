# Day 07 - f-Strings and Recursion

# -----------------------------------
# f-Strings
# -----------------------------------

name = "Alex"                             # Store name
course = "Python"                         # Store course
age = 20                                  # Store age

print(f"Name : {name}")                   # Display name
print(f"Course : {course}")               # Display course
print(f"Age : {age}")                     # Display age

marks = 85                                # Store marks

print(f"Marks : {marks}")                 # Display marks
print(f"Next Marks : {marks + 5}")        # Evaluate expression


# -----------------------------------
# Recursion
# -----------------------------------

# Countdown using recursion
def countdown(number):

    if number == 0:                       # Base condition
        print("Done")
        return

    print(number)                         # Display number
    countdown(number - 1)                 # Function calls itself


countdown(5)


# -----------------------------------
# Factorial using Recursion
# -----------------------------------

def factorial(number):

    if number == 1:                       # Base condition
        return 1

    return number * factorial(number - 1) # Recursive call


result = factorial(5)                     # Store result

print(result)                             # Display factorial
