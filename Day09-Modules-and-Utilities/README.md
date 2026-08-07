# Day 09 - Shorthand Operators, enumerate() and Importing Modules 🐍

## Introduction

On the ninth day of my Python learning journey, I learned about **Shorthand Operators**, the **enumerate() function**, and different ways to **import modules** in Python. These concepts help write cleaner code, work with loops more efficiently, and reuse Python's built-in modules.

---

# 1. Shorthand Operators

Shorthand operators are a shorter way of performing operations and updating the value of a variable.

## Common Shorthand Operators

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 2` | `x = x ** 2` |

## Example

```python
number = 10

number += 5

print(number)
```

### Output

```
15
```

### Explanation

The `+=` operator adds the value and stores the updated result in the same variable.

---

# 2. enumerate() Function

The `enumerate()` function is used to get both the **index** and the **value** while looping through an iterable like a list or tuple.

## Syntax

```python
enumerate(iterable)
```

## Example

```python
fruits = ["Apple", "Banana", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### Output

```
0 Apple
1 Banana
2 Orange
```

### Explanation

`enumerate()` returns both the index and the corresponding value during each iteration.

---

# 3. Importing Modules

A module is a Python file that contains functions and variables. Python provides many built-in modules that can be imported and used in programs.

## Different Ways to Import Modules

### Import the entire module

```python
import math
```

### Import a specific function

```python
from math import sqrt
```

### Import all functions

```python
from math import *
```

### Import using an alias

```python
import math as m
```

### Display all available functions

```python
import math

print(dir(math))
```

---

# Key Learnings

- Learned how shorthand operators simplify assignments.
- Used the `enumerate()` function to access indexes while looping.
- Learned different ways to import Python modules.
- Imported specific functions from a module.
- Used aliases while importing modules.
- Explored module contents using `dir()`.
