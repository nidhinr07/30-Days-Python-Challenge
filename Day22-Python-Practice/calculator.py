# Day 22 - Calculator


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation: ")

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        try:
            print("Result:", divide(num1, num2))

        except ZeroDivisionError:
            print("Cannot divide by zero.")

    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter valid numbers.")
