# Day 08 - Exception Handling 🐍

## Introduction

On the eighth day of my Python learning journey, I learned about **Exception Handling**, **Raising Custom Exceptions**, and **Common Python Exceptions**. Exception handling helps prevent a program from crashing when an error occurs. Instead of stopping the program, Python allows us to handle errors gracefully using `try` and `except` blocks.

---

# 1. Exception Handling

An **exception** is an error that occurs while a program is running. Using `try` and `except`, we can catch these errors and display a user-friendly message instead of terminating the program.

## Syntax

```python
try:
    # Code that may cause an error

except:
    # Code to handle the error
```

## Example

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")
```

### Output

```
Enter a number: 0
Cannot divide by zero.
```

### Explanation

The program checks for possible errors. If the user enters **0**, a `ZeroDivisionError` occurs. If the user enters text instead of a number, a `ValueError` occurs. The program handles both errors without crashing.

---

# 2. Raising Custom Exceptions

Python allows us to create our own exceptions using the `raise` keyword. This is useful when we want to stop the program based on our own conditions.

## Syntax

```python
raise Exception("Error Message")
```

## Example

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")
```

### Output

```
ValueError: Age must be 18 or above.
```

### Explanation

The program checks the age. Since the age is less than **18**, it raises a custom `ValueError` with the specified message.

---

# 3. Common Python Exceptions

Python provides many built-in exceptions. Some of the most commonly used exceptions are:

| Exception | Description |
|-----------|-------------|
| `ValueError` | Invalid value is provided. |
| `TypeError` | Invalid data type is used. |
| `NameError` | Variable is not defined. |
| `IndexError` | List index is out of range. |
| `KeyError` | Dictionary key is not found. |
| `ZeroDivisionError` | Division by zero occurs. |
| `FileNotFoundError` | File does not exist. |

---

# Key Learnings

- Learned what an exception is.
- Used `try` and `except` to handle errors.
- Handled different types of exceptions.
- Learned how to raise custom exceptions using `raise`.
- Explored commonly used Python exceptions.
- Understood how exception handling makes programs more reliable.
