# Day 01 - Python Introduction 🐍

## Introduction

On the first day of my Python learning journey, I started with the basic concepts of Python programming. I learned how to display output, write comments, take input from users, and use some important formatting features in Python.

These concepts are the foundation for understanding and writing Python programs.

## Topics Learned

* Basic Print Statement
* Single Line Comments
* Multi-Line Comments
* Escape Sequences
* New Line Character (`\n`)
* `sep` Parameter in Print Function
* `end` Parameter in Print Function
* Getting User Input using `input()`

---

# 1. Basic Print Statement

The `print()` function is used to display information on the screen.

Example:

```python
print("Hello Python")
```

Output:

```
Hello Python
```

---

# 2. Comments in Python

Comments are used to write notes inside the code. They help programmers understand the code better, and Python ignores them while executing the program.

## Single Line Comment

A single line comment starts with the `#` symbol.

Example:

```python
# This is a comment
print("Learning Python")
```

## Multi-Line Comment

Multi-line comments are generally written using triple quotes (`"""` or `'''`).

Example:

```python
"""
This is a multi-line comment.
It can contain multiple lines.
"""
print("Python")
```

---

# 3. Escape Sequences

Escape sequences are special characters used inside strings to perform specific actions.

## New Line (`\n`)

`\n` is used to print text in the next line.

Example:

```python
print("Hello\nPython")
```

Output:

```
Hello
Python
```

---

# 4. sep Parameter

The `sep` parameter is used to define how multiple values are separated in a print statement.

Example:

```python
print("Python", "Java", "C++", sep="-")
```

Output:

```
Python-Java-C++
```

---

# 5. end Parameter

The `end` parameter controls what happens after a print statement.

By default, `print()` moves to the next line.

Example:

```python
print("Hello", end=" ")
print("Python")
```

Output:

```
Hello Python
```

---

# 6. Getting User Input

The `input()` function is used to get information from the user.

Example:

```python
name = input("Enter your name: ")

print("Welcome", name)
```

Output:

```
Enter your name: Nidhin
Welcome Nidhin
```

By default, input values are stored as strings. We can convert them into other data types when required.

Example:

```python
age = int(input("Enter your age: "))

print(age)
```

---

## Key Learnings

Today I learned the basic building blocks of Python:

* How to display output using `print()`
* How to write comments
* How escape sequences work
* How to format output using `sep` and `end`
* How to interact with users using `input()`

These concepts are the first steps towards learning Python programming.
