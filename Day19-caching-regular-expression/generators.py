# Day 19 - Python Generators


# -----------------------------------
# Basic Generator
# -----------------------------------

def numbers():
    yield 1                              # Produce first value
    yield 2                              # Produce second value
    yield 3                              # Produce third value


result = numbers()                      # Create generator object

print(next(result))                     # Get first value
print(next(result))                     # Get second value
print(next(result))                     # Get third value


# -----------------------------------
# Generator with Loop
# -----------------------------------

def count_numbers():
    for number in range(1, 6):
        yield number                     # Produce number one by one


for number in count_numbers():
    print(number)                        # Display generated value
