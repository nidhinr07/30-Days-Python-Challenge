# Day 13 - Introduction to OOP 🐍

## Introduction

On the thirteenth day of my Python learning journey, I started learning the basics of **Object-Oriented Programming (OOP)**.

OOP is a programming approach that organizes programs using **classes and objects**. It helps make code more organized, reusable, and easier to manage.

---

## 1. What is OOP?

**OOP (Object-Oriented Programming)** is a programming concept where programs are designed around objects and classes.

An object can contain:

* Data
* Methods that work with the data

Python supports Object-Oriented Programming.

---

## 2. What is a Class?

A **class** is a blueprint or template used to create objects.

For example, a `Student` class can define the properties and methods that student objects can have.

```python
class Student:
    pass
```

### Explanation

A class defines the structure that objects created from it can use.

---

## 3. What is an Object?

An **object** is an instance of a class.

If `Student` is a class, an individual object can be created from that class.

```python
student = Student()
```

### Explanation

`Student()` creates an object from the `Student` class.

---

## 4. Self Parameter

`self` refers to the **current object** of a class.

It is used to access the attributes and methods that belong to that object.

```python
class Student:

    def show(self):
        print("Student details")
```

### Explanation

Here, `self` refers to the object that calls the `show()` method.

---

## 5. Constructor

A **constructor** is a special method that runs automatically when an object is created.

In Python, the constructor is written using the `__init__()` method.

```python
class Student:

    def __init__(self):
        print("Object created")
```

When an object is created:

```python
student = Student()
```

The `__init__()` method runs automatically.

---

## 6. **init**() Method

The `__init__()` method is used to initialize the attributes of an object when it is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Explanation

`self.name` and `self.age` store values inside the current object.

---

## 7. Types of Constructors

The two basic types of constructors covered are:

1. Default Constructor
2. Parameterized Constructor

---

### Default Constructor

A **default constructor** does not require additional values when the object is created.

```python
class Student:

    def __init__(self):
        self.name = "Student"
```

### Explanation

The object receives a predefined value when it is created.

---

### Parameterized Constructor

A **parameterized constructor** accepts values when the object is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

An object can be created by passing values:

```python
student = Student("Student", 20)
```

### Explanation

The values are passed to the constructor while creating the object.

---

# Four Pillars of OOP

Object-Oriented Programming is commonly explained using four main pillars.

---

## 1. Encapsulation

**Encapsulation** means combining data and the methods that work with that data inside a class.

It also helps control how the data is accessed.

### Simple idea

```text
Data + Methods = Encapsulation
```

---

## 2. Inheritance

**Inheritance** allows one class to acquire properties and methods from another class.

### Simple idea

```text
Parent Class → Child Class
```

It helps with code reuse.

---

## 3. Polymorphism

**Polymorphism** means that the same method or interface can behave differently depending on the object or situation.

### Simple idea

```text
One interface → Different behaviours
```

---

## 4. Abstraction

**Abstraction** means hiding unnecessary implementation details and showing only the important features.

### Simple idea

```text
Hide unnecessary details → Show essential features
```

---

# Class vs Object

| Class                                    | Object                         |
| ---------------------------------------- | ------------------------------ |
| Blueprint or template                    | Instance of a class            |
| Defines structure                        | Uses the structure             |
| Does not represent one specific instance | Represents a specific instance |
| Used to create objects                   | Created from a class           |

---

# Key Learnings

* Learned the basic concept of OOP.
* Understood what a class is.
* Learned what an object is.
* Understood the `self` parameter.
* Learned about constructors.
* Learned the `__init__()` method.
* Learned about default constructors.
* Learned about parameterized constructors.
* Got an introduction to the four pillars of OOP.
* Learned about encapsulation.
* Learned about inheritance.
* Learned about polymorphism.
* Learned about abstraction.

---

# Note

This day focuses on the **basic introduction to Object-Oriented Programming**. More practical OOP concepts and coding examples will be explored in the upcoming days.
