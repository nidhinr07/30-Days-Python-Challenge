# Day 12 - Lambda, Map, Filter, Reduce and Is Operator 🐍

## Introduction

On the twelfth day of my Python learning journey, I learned about **Lambda Functions**, the `map()`, `filter()`, and `reduce()` functions, and the difference between the `==` and `is` operators.

These concepts helped me understand shorter functions, processing collections, filtering values, reducing data, and checking object identity.

---

# 1. Lambda Function

A **lambda function** is a small anonymous function written in a single line.

## Syntax

```python
lambda arguments: expression
```

## Example

```python
square = lambda x: x * x

print(square(5))
```

### Output

```text
25
```

### Explanation

The lambda function takes `x` and returns its square.

---

# 2. map()

The `map()` function applies a function to every item in an iterable.

## Syntax

```python
map(function, iterable)
```

## Example

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

### Output

```text
[1, 4, 9, 16]
```

### Explanation

`map()` applies the lambda function to every number in the list.

---

# 3. filter()

The `filter()` function selects elements that satisfy a condition.

## Syntax

```python
filter(function, iterable)
```

## Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

### Output

```text
[2, 4, 6]
```

### Explanation

`filter()` keeps only the numbers that satisfy the condition.

---

# 4. reduce()

The `reduce()` function repeatedly applies a function to the elements and produces a single result.

`reduce()` is available from the `functools` module.

## Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)

print(total)
```

### Output

```text
10
```

### Explanation

The values are combined step by step to produce one final result.

---

# 5. == Operator

The `==` operator checks whether two values are equal.

## Example

```python
a = 10
b = 10

print(a == b)
```

### Output

```text
True
```

### Explanation

Both variables contain equal values, so the result is `True`.

---

# 6. is Operator

The `is` operator checks whether two variables refer to the **same object**.

## Example

```python
a = [1, 2, 3]
b = a

print(a is b)
```

### Output

```text
True
```

### Explanation

Both variables refer to the same list object.

---

# 7. Difference Between == and is

| Operator | Checks |
|----------|--------|
| `==` | Whether values are equal |
| `is` | Whether objects are the same |

## Example

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

### Output

```text
True
False
```

### Explanation

The two lists contain the same values, so `==` returns `True`. However, they are two different list objects, so `is` returns `False`.

---

# Key Learnings

- Learned how to create lambda functions.
- Used `map()` to transform values.
- Used `filter()` to select values.
- Used `reduce()` to combine values into one result.
- Learned how `==` compares values.
- Learned how `is` checks object identity.
- Understood the difference between equality and identity.
