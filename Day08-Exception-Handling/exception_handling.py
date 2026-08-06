# Day 08 - Exception Handling

# -----------------------------------
# Basic try and except
# -----------------------------------

try:
    number = int(input("Enter a number: "))      # Get user input

    print(100 / number)                          # Divide 100 by number

except:
    print("Something went wrong.")               # Handle any error


# -----------------------------------
# Handling ZeroDivisionError
# -----------------------------------

try:
    number = int(input("\nEnter a number: "))    # Get user input

    print(100 / number)                          # Divide number

except ZeroDivisionError:
    print("Cannot divide by zero.")              # Handle zero division


# -----------------------------------
# Handling ValueError
# -----------------------------------

try:
    age = int(input("\nEnter your age: "))       # Get integer input

    print(f"Age : {age}")

except ValueError:
    print("Please enter numbers only.")          # Handle invalid input


# -----------------------------------
# Handling Multiple Exceptions
# -----------------------------------

try:
    number = int(input("\nEnter a number: "))    # Get user input

    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Enter numbers only.")


# -----------------------------------
# Using else
# -----------------------------------

try:
    number = int(input("\nEnter a number: "))    # Get user input

    result = 50 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result :", result)                    # Runs if no error


# -----------------------------------
# Using finally
# -----------------------------------

try:
    file = open("sample.txt", "r")               # Open file

    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")                   # Always executes
