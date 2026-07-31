# Day 02 - Data Types, Type Casting, Strings and Conditional Statements 🐍

## Introduction

On the second day of my Python learning journey, I explored Python data types, type casting, string operations, and conditional statements. These concepts are important because they help us store different kinds of data, manipulate text, and make decisions in a program.

---

# 1. Data Types

A **data type** defines the kind of value stored in a variable. Python automatically identifies the data type based on the assigned value.

## Numeric Data Type

Numeric data types are used to store numbers. They are mainly used for mathematical calculations.

Python provides three numeric data types:

* **int** → Stores whole numbers.
* **float** → Stores decimal numbers.
* **complex** → Stores complex numbers.

### Example

```python
age = 20
price = 99.99

print(type(age))
print(type(price))
```

### Output

```text
<class 'int'>
<class 'float'>
```

### Explanation

* `20` is an integer, so Python stores it as **int**.
* `99.99` contains a decimal value, so Python stores it as **float**.
* The `type()` function returns the data type of a variable.

---

## Text Data Type

The **str** (string) data type is used to store text.

### Example

```python
language = "Python"

print(type(language))
```

### Output

```text
<class 'str'>
```

### Explanation

Since `"Python"` is enclosed inside quotation marks, Python treats it as a string.

---

## Boolean Data Type

The Boolean data type stores only two values:

* `True`
* `False`

It is mainly used in conditions and comparisons.

### Example

```python
is_logged_in = True

print(type(is_logged_in))
```

### Output

```text
<class 'bool'>
```

### Explanation

The value `True` belongs to the Boolean (`bool`) data type.

---

# 2. Type Casting

Type casting means converting one data type into another.

Python supports two types of type casting.

## Implicit Type Casting

Implicit type casting happens automatically when Python converts one data type into another.

### Example

```python
number = 10
price = 2.5

result = number + price

print(result)
print(type(result))
```

### Output

```text
12.5
<class 'float'>
```

### Explanation

Python automatically converts the integer into a float before performing the calculation.

---

## Explicit Type Casting

Explicit type casting is done manually using functions like `int()`, `float()`, and `str()`.

### Example

```python
number = "100"

print(int(number))
```

### Output

```text
100
```

### Explanation

The string `"100"` is manually converted into an integer using `int()`.

---

# 3. Finding the Length of a String

The `len()` function returns the total number of characters present in a string.

### Example

```python
language = "Python"

print(len(language))
```

### Output

```text
6
```

### Explanation

The word **Python** contains six characters, so `len()` returns **6**.

---

# 4. String Methods

String methods are built-in functions that help us perform different operations on strings.

| Method          | Description                                            |
| --------------- | ------------------------------------------------------ |
| `upper()`       | Converts all letters to uppercase                      |
| `lower()`       | Converts all letters to lowercase                      |
| `strip()`       | Removes spaces from both ends                          |
| `rstrip()`      | Removes spaces from the right side                     |
| `replace()`     | Replaces one value with another                        |
| `capitalize()`  | Capitalizes the first letter                           |
| `center()`      | Aligns the string at the center                        |
| `count()`       | Counts the occurrences of a value                      |
| `endswith()`    | Checks whether a string ends with a specific value     |
| `find()`        | Returns the first occurrence of a value                |
| `index()`       | Returns the index of a value                           |
| `isalnum()`     | Checks whether all characters are letters or numbers   |
| `isalpha()`     | Checks whether all characters are alphabets            |
| `islower()`     | Checks whether all letters are lowercase               |
| `isprintable()` | Checks whether all characters are printable            |
| `isspace()`     | Checks whether the string contains only spaces         |
| `istitle()`     | Checks whether every word starts with a capital letter |
| `isupper()`     | Checks whether all letters are uppercase               |
| `startswith()`  | Checks whether a string starts with a specific value   |
| `swapcase()`    | Converts uppercase letters to lowercase and vice versa |
| `title()`       | Converts the first letter of every word to uppercase   |

---

# 5. Conditional Statements

Conditional statements help a program make decisions based on a condition.

## if Statement

Executes a block of code only when the condition is `True`.

## if-else Statement

Executes one block if the condition is `True`, otherwise executes another block.

## Nested if Statement

A nested `if` statement is an `if` statement inside another `if` statement. It is useful when multiple conditions need to be checked.

---

## Key Learnings

* Learned different Python data types.
* Understood implicit and explicit type casting.
* Learned how to find the length of a string using `len()`.
* Explored commonly used string methods.
* Practiced writing programs using `if`, `if-else`, and nested `if` statements.
