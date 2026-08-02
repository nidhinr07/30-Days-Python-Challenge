# Day 04 - Functions 🐍

## Introduction

On the fourth day of my Python learning journey, I learned about **functions**, one of the most important concepts in Python. Functions help us organize code into reusable blocks, making programs easier to read, maintain, and reuse. I also learned different types of function arguments and how to return values from a function.

---

# 1. What is a Function?

A **function** is a block of code that performs a specific task. Instead of writing the same code multiple times, we can write it once inside a function and call it whenever needed.

Functions improve code readability, reduce repetition, and make programs easier to manage.

---

# 2. Built-in Functions

Built-in functions are functions that are already available in Python. They can be used directly without creating them.

Some common built-in functions are:

* `print()`
* `input()`
* `len()`
* `type()`
* `int()`
* `float()`
* `str()`

### Example

```python
name = "Python"

print(len(name))
print(type(name))
```

### Output

```text
6
<class 'str'>
```

### Explanation

* `len()` returns the number of characters in the string.
* `type()` returns the data type of the variable.

---

# 3. User-defined Functions

A user-defined function is a function created by the programmer using the `def` keyword.

### Syntax

```python
def function_name():
    # Code
```

### Example

```python
def greet():
    print("Welcome to Python")

greet()
```

### Output

```text
Welcome to Python
```

### Explanation

The function is created using `def` and executes when it is called.

---

# 4. Function Arguments

Arguments are values passed to a function when it is called. They allow the function to work with different data.

---

## Positional Arguments

In positional arguments, values are assigned based on their position.

### Example

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Output

```text
30
```

### Explanation

`10` is assigned to `a` and `20` is assigned to `b` based on their position.

---

## Keyword Arguments

In keyword arguments, values are assigned using the parameter names. The order does not matter.

### Example

```python
def student(name, course):
    print(name)
    print(course)

student(course="Python", name="Alex")
```

### Output

```text
Alex
Python
```

### Explanation

The values are assigned using parameter names instead of position.

---

## Variable Length Arguments

Sometimes we do not know how many arguments will be passed to a function. In such cases, we use `*args`.

### Example

```python
def numbers(*values):
    print(values)

numbers(10, 20, 30, 40)
```

### Output

```text
(10, 20, 30, 40)
```

### Explanation

`*args` collects all values into a tuple.

---

# 5. Return Statement

The `return` statement sends a value back to the place where the function was called.

### Example

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

### Output

```text
25
```

### Explanation

The function calculates the square of the number and returns the result.

---

## Key Learnings

* Learned what a function is.
* Understood built-in and user-defined functions.
* Learned how to pass arguments to functions.
* Explored positional, keyword, and variable-length arguments.
* Learned how the `return` statement works.
