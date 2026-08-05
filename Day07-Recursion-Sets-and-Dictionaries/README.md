# Day 07 - Recursion, Sets, and Dictionaries 🐍

## Introduction

On the seventh day of my Python learning journey, I explored **f-strings**, **recursion**, **sets**, and **dictionaries**. These concepts helped me understand better ways to format strings, solve problems using recursive functions, store unique values using sets, and manage data efficiently using dictionaries.

---

# 1. f-Strings

An **f-string** (formatted string literal) is a simple and readable way to insert variables or expressions inside a string. It makes string formatting easier compared to older methods.

## Syntax

```python
name = "Alex"

print(f"Hello, {name}")
```

### Output

```
Hello, Alex
```

### Explanation

The variable `name` is placed directly inside the string using curly braces `{}`.

---

# 2. Recursion

Recursion is a programming technique where a function calls itself to solve a problem. Every recursive function must have a **base case** to stop the recursion.

## Syntax

```python
def function():
    function()
```

## Example

```python
def countdown(number):

    if number == 0:
        print("Done")
        return

    print(number)
    countdown(number - 1)

countdown(5)
```

### Output

```
5
4
3
2
1
Done
```

### Explanation

The function keeps calling itself until the value becomes `0`. When the base case is reached, the recursion stops.

---

# 3. Sets

A **set** is an unordered collection of unique elements. Duplicate values are automatically removed.

## Syntax

```python
numbers = {10, 20, 30}
```

## Example

```python
numbers = {10, 20, 20, 30}

print(numbers)
```

### Output

```
{10, 20, 30}
```

### Explanation

The duplicate value `20` is removed because a set stores only unique elements.

---

# 4. Set Methods

Some commonly used set methods are:

## add()

Adds a single element to a set.

```python
numbers.add(40)
```

---

## update()

Adds multiple elements to a set.

```python
numbers.update([50, 60])
```

---

## remove()

Removes a specified element.

```python
numbers.remove(20)
```

---

## discard()

Removes an element without raising an error if it does not exist.

```python
numbers.discard(100)
```

---

## pop()

Removes and returns a random element.

```python
numbers.pop()
```

---

## union()

Combines two sets.

```python
set1.union(set2)
```

---

## intersection()

Returns common elements between two sets.

```python
set1.intersection(set2)
```

---

# 5. Dictionaries

A **dictionary** stores data as **key-value pairs**. Each key is unique and is used to access its corresponding value.

## Syntax

```python
student = {
    "name": "Alex",
    "age": 20
}
```

## Example

```python
student = {
    "name": "Alex",
    "age": 20
}

print(student["name"])
```

### Output

```
Alex
```

### Explanation

The value is accessed using its key.

---

# 6. Dictionary Methods

Some commonly used dictionary methods are:

## keys()

Returns all keys.

```python
student.keys()
```

---

## values()

Returns all values.

```python
student.values()
```

---

## items()

Returns key-value pairs.

```python
student.items()
```

---

## get()

Returns the value of a key.

```python
student.get("name")
```

---

## update()

Updates an existing key or adds a new key.

```python
student.update({"age": 21})
```

---

## pop()

Removes a key-value pair.

```python
student.pop("age")
```

---

## clear()

Removes all items from the dictionary.

```python
student.clear()
```

---

# Key Learnings

- Learned how to use **f-strings** for string formatting.
- Understood how **recursion** works with a base case.
- Created and modified **sets**.
- Practiced commonly used **set methods**.
- Learned how **dictionaries** store data using key-value pairs.
- Explored important **dictionary methods** for accessing and updating data.
