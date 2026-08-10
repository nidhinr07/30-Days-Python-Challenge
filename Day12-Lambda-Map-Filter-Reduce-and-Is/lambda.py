# Day 12 - Lambda Functions


# -----------------------------------
# Basic Lambda Function
# -----------------------------------

square = lambda x: x * x                    # Create square function

print(square(5))                            # Display square


# -----------------------------------
# Lambda with Two Arguments
# -----------------------------------

add = lambda a, b: a + b                    # Add two values

print(add(10, 20))                          # Display result


# -----------------------------------
# Lambda with Three Arguments
# -----------------------------------

total = lambda a, b, c: a + b + c           # Add three values

print(total(10, 20, 30))                    # Display total


# -----------------------------------
# Lambda with Condition
# -----------------------------------

check = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check(10))                            # Check number
print(check(7))                             # Check number


# -----------------------------------
# Lambda with String
# -----------------------------------

length = lambda text: len(text)             # Find string length

print(length("Python"))                     # Display length
