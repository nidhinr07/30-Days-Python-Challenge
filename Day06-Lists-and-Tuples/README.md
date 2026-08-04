# Day 06 - Lists and Tuples 🐍

## Introduction

On the sixth day of my Python learning journey, I learned about **Lists** and **Tuples**, two important data structures in Python. Lists are used to store multiple values in a single variable and can be modified after creation. Tuples are similar to lists but are immutable, meaning their values cannot be changed once created.

I also explored commonly used list methods, list comprehensions, and tuple methods.

---

# 1. Lists

A **list** is an ordered collection that can store multiple values of different data types. Lists are mutable, which means elements can be added, removed, or modified.

## Syntax

```python
fruits = ["Apple", "Banana", "Orange"]
```

## Example

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits)
```

### Output

```
['Apple', 'Banana', 'Orange']
```

### Explanation

The list stores three string values in a single variable.

---

# 2. Accessing List Elements

Each element in a list has an index.

- Positive indexing starts from **0**.
- Negative indexing starts from **-1**.

## Example

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
print(fruits[-1])
```

### Output

```
Apple
Orange
```

### Explanation

`fruits[0]` returns the first element, while `fruits[-1]` returns the last element.

---

# 3. List Slicing

Slicing is used to access multiple elements from a list.

## Syntax

```python
list[start:stop]
```

## Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

### Output

```
[20, 30, 40]
```

### Explanation

The slice starts from index **1** and stops before index **4**.

---

# 4. List Methods

## append()

Adds a single element to the end of the list.

```python
numbers.append(60)
```

---

## extend()

Adds multiple elements to the list.

```python
numbers.extend([70, 80])
```

---

## insert()

Inserts an element at a specific position.

```python
numbers.insert(2, 25)
```

---

## remove()

Removes a specific element.

```python
numbers.remove(30)
```

---

## pop()

Removes the last element by default.

```python
numbers.pop()
```

---

## sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

---

## reverse()

Reverses the order of the list.

```python
numbers.reverse()
```

---

## count()

Counts how many times an element appears.

```python
numbers.count(20)
```

---

# 5. List Comprehension

List comprehension is a short and simple way to create lists.

## Syntax

```python
[expression for item in iterable]
```

## Example

```python
square = [x * x for x in range(1, 6)]

print(square)
```

### Output

```
[1, 4, 9, 16, 25]
```

### Explanation

The loop creates a new list containing the square of each number.

---

# 6. Tuples

A **tuple** is an ordered collection that stores multiple values. Unlike lists, tuples are immutable, meaning they cannot be modified after creation.

## Syntax

```python
colors = ("Red", "Green", "Blue")
```

## Example

```python
colors = ("Red", "Green", "Blue")

print(colors)
```

### Output

```
('Red', 'Green', 'Blue')
```

### Explanation

A tuple stores multiple values just like a list, but its elements cannot be changed.

---

# 7. Accessing Tuple Elements

Tuple elements are accessed using indexes.

## Example

```python
colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[-1])
```

### Output

```
Red
Blue
```

---

# 8. Tuple Methods

Tuples have only two commonly used methods.

## count()

Returns the number of occurrences of a value.

```python
numbers = (10, 20, 20, 30)

print(numbers.count(20))
```

### Output

```
2
```

---

## index()

Returns the index of the first occurrence.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

### Output

```
1
```

---

# Key Learnings

- Learned how to create and use lists.
- Accessed list elements using indexing.
- Used slicing to retrieve multiple elements.
- Practiced commonly used list methods.
- Learned how list comprehensions simplify list creation.
- Understood tuples and their immutable nature.
- Explored tuple methods like `count()` and `index()`.
