# Day 03 - Match Case Statements and Loops

# Match Case Statement
day = 2                      # Store day number

match day:
    case 1:
        print("Monday")      # Case one
    case 2:
        print("Tuesday")     # Case two
    case 3:
        print("Wednesday")   # Case three
    case _:
        print("Invalid Day") # Default case


# For Loop
for number in range(1, 6):   # Loop from 1 to 5
    print(number)            # Display number


# Range Function
print(range(5))              # Display range object

for value in range(2, 11, 2): # Start, stop, step
    print(value)             # Display even numbers


# While Loop
count = 1                    # Starting value

while count <= 5:            # Loop condition
    print(count)             # Display count
    count += 1               # Increase count


# Break Statement
for number in range(1, 6):   # Loop from 1 to 5

    if number == 4:          # Stop at four
        break

    print(number)            # Display number


# Continue Statement
for number in range(1, 6):   # Loop from 1 to 5

    if number == 3:          # Skip number three
        continue

    print(number)            # Display remaining numbers
