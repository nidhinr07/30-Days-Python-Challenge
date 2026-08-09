# Day 11 - Local and Global Variables


# -----------------------------------
# Local Variable
# -----------------------------------

def show_name():

    name = "Alex"                          # Local variable

    print(name)                            # Access local variable


show_name()


# -----------------------------------
# Global Variable
# -----------------------------------

name = "Python"                            # Global variable


def show_language():

    print(name)                            # Access global variable


show_language()


# -----------------------------------
# Local and Global Variables
# -----------------------------------

number = 100                               # Global variable


def calculate():

    number = 50                            # Local variable

    print(number)                          # Access local value


calculate()

print(number)                              # Access global value


# -----------------------------------
# Using global Keyword
# -----------------------------------

count = 10                                 # Global variable


def update_count():

    global count                            # Use global variable

    count += 5                              # Update global value


update_count()

print(count)                                # Display updated value
```

### Topics covered

- `Local variable`
- `Global variable`
- Difference between local and global scope
- `global` keyword
- Updating a global variable inside a function

Next: **`file_handling.py`** — all the file I/O concepts from Day 11.
