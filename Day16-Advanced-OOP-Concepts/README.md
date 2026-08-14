# Day 16 - Advanced OOP Concepts 🐍

## Introduction

On the sixteenth day of my Python learning journey, I learned some additional OOP concepts and useful built-in functions.

The topics covered today are **decorators, instance and class variables, class methods, static methods, `dir()`, `__dict__`, `help()`, `super()`, and magic/dunder methods**.

---

# 1. Python Decorators

A **decorator** is a function that allows us to modify or extend the behavior of another function without changing its original code.

### Basic Example

```python
def decorator_function(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator_function
def say_hello():
    print("Hello Python")


say_hello()
```

The `@decorator_function` syntax applies the decorator to `say_hello()`.

---

# 2. Instance Variables

**Instance variables** belong to a particular object.

They are usually created using `self`.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each object can have a different value.

---

# 3. Class Variables

**Class variables** belong to the class and are shared by its objects.

```python
class Student:

    school = "Python School"
```

The variable `school` is shared by objects of the class.

---

# 4. Instance Variables vs Class Variables

| Instance Variable                         | Class Variable                |
| ----------------------------------------- | ----------------------------- |
| Belongs to an object                      | Belongs to the class          |
| Created using `self`                      | Created inside the class      |
| Can have different values for each object | Usually shared by all objects |

---

# 5. Class Method

A **class method** works with the class rather than a particular object.

It uses the `@classmethod` decorator and receives `cls` as its first parameter.

```python
class Student:

    school = "Python School"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

---

# 6. Class Method as Alternative Constructor

A class method can also be used as an **alternative constructor**.

This allows objects to be created in another way.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Alex-20")
```

Here, `from_string()` provides another way to create a `Student` object.

---

# 7. Static Method

A **static method** belongs to a class but does not require `self` or `cls`.

It is created using `@staticmethod`.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

A static method does not depend on instance or class data.

---

# 8. dir()

The `dir()` function returns a list of attributes and methods available for an object or class.

```python
numbers = [1, 2, 3]

print(dir(numbers))
```

It can be useful when exploring what methods are available.

---

# 9. **dict**

`__dict__` shows the attributes stored by an object or class.

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Alex")

print(student.__dict__)
```

It can show the object's stored attributes.

---

# 10. help()

The `help()` function provides information about Python objects, classes, functions, and modules.

```python
help(str)
```

It can be useful when learning how a Python feature works.

---

# 11. super()

The `super()` function is used to access methods or attributes from a parent class.

```python
class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        super().show()
        print("Child method")


child = Child()

child.show()
```

Here, `super()` is used to call the parent class method.

---

# 12. Magic / Dunder Methods

**Magic methods**, also called **dunder methods**, are special methods whose names start and end with double underscores.

Examples:

```text
__init__
__str__
__len__
__add__
```

### Example: **str**()

The `__str__()` method controls what is displayed when an object is converted to a string.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Alex")

print(student)
```

### Example: **len**()

The `__len__()` method can define what happens when `len()` is used with an object.

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Alex", "Sam", "John"])

print(len(team))
```

---

# Key Learnings

* Learned Python decorators.
* Understood instance variables.
* Understood class variables.
* Learned the difference between instance and class variables.
* Learned class methods.
* Learned class methods as alternative constructors.
* Learned static methods.
* Learned how to use `dir()`.
* Learned how to use `__dict__`.
* Learned how to use `help()`.
* Learned the `super()` keyword.
* Learned about magic/dunder methods.
* Practiced `__str__()` and `__len__()`.

---

# Note

These concepts extend the OOP fundamentals learned in the previous days and provide a better understanding of how Python classes and objects work internally.
