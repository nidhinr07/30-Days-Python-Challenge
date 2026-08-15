# Day 17 - Operator Overloading


# Addition operator overloading
class Number:

    def __init__(self, value):
        self.value = value                    # Store number value

    def __add__(self, other):
        return self.value + other.value       # Add object values


num1 = Number(10)                             # Create first object
num2 = Number(20)                             # Create second object

print(num1 + num2)                            # Use addition operator


# Subtraction operator overloading
class Calculator:

    def __init__(self, value):
        self.value = value                    # Store calculator value

    def __sub__(self, other):
        return self.value - other.value       # Subtract object values


num1 = Calculator(30)                         # Create first object
num2 = Calculator(10)                         # Create second object

print(num1 - num2)                            # Use subtraction operator


# Equality operator overloading
class Score:

    def __init__(self, marks):
        self.marks = marks                    # Store marks value

    def __eq__(self, other):
        return self.marks == other.marks      # Compare object values


score1 = Score(80)                            # Create first score
score2 = Score(80)                            # Create second score

print(score1 == score2)                       # Compare object values
