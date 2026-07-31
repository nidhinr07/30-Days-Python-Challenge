# Numeric Data Types
age = 20                 # Integer value
price = 99.99            # Float value
complex_num = 2 + 3j     # Complex value

print(type(age))         # Display integer type
print(type(price))       # Display float type
print(type(complex_num)) # Display complex type


# Text Data Type
language = "Python"      # String value

print(language)          # Display string
print(type(language))    # Display string type
print(len(language))     # Count characters


# Boolean Data Type
is_logged_in = True      # Boolean value

print(type(is_logged_in)) # Display boolean type


# Implicit Type Casting
number = 10              # Integer value
decimal = 2.5            # Float value

result = number + decimal  # Automatic conversion

print(result)            # Display result
print(type(result))      # Display result type


# Explicit Type Casting
value = "100"            # String value

print(int(value))        # Convert to integer
print(float(value))      # Convert to float


# String Methods
text = "  python programming  "  # Sample string

print(text.upper())      # Convert to uppercase
print(text.lower())      # Convert to lowercase
print(text.strip())      # Remove extra spaces
print(text.replace("python", "Java"))  # Replace word
print(text.capitalize()) # Capitalize first letter
print(text.count("m"))   # Count occurrences
print(text.endswith("g  ")) # Check ending
print(text.find("program")) # Find position
print(text.index("python")) # Exact index
print(text.islower())    # Check lowercase
print(text.isalpha())    # Check alphabets
print(text.startswith(" ")) # Check beginning
print(text.swapcase())   # Swap letter cases
print(text.title())      # Convert to title case


# If Statement
marks = 75               # Store marks

if marks >= 50:
    print("Pass")        # Display pass


# If-Else Statement
number = 8               # Store number

if number % 2 == 0:
    print("Even")        # Even number
else:
    print("Odd")         # Odd number


# Nested If Statement
age = 20                 # Store age

if age >= 18:
    if age >= 21:
        print("Eligible")  # Eligible
    else:
        print("Adult")     # Adult
else:
    print("Minor")         # Minor
