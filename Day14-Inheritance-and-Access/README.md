# Day 14 - Inheritance and Access Specifiers 🐍

## Introduction

On the fourteenth day of my Python learning journey, I learned about **Inheritance** and the different types of inheritance.

I also learned the basic idea of **access specifiers**, **getters**, and **setters** in Python.

---

# 1. What is Inheritance?

**Inheritance** is an OOP concept where one class can acquire properties and methods from another class.

It helps with **code reusability** and allows us to create a relationship between classes.

### Simple Idea

```text
Parent Class
     ↓
Child Class
```

The child class can use the properties and methods of the parent class.

---

# 2. Types of Inheritance

There are five commonly discussed types of inheritance:

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

---

## 2.1 Single Inheritance

In **single inheritance**, one child class inherits from one parent class.

```text
Parent
  ↓
Child
```

### Example Idea

A `Dog` class inherits from an `Animal` class.

---

## 2.2 Multiple Inheritance

In **multiple inheritance**, one child class inherits from more than one parent class.

```text
Parent 1 ──┐
           ↓
         Child
           ↑
Parent 2 ──┘
```

### Example Idea

A `Child` class can inherit features from both `Father` and `Mother`.

---

## 2.3 Multilevel Inheritance

In **multilevel inheritance**, a class inherits from another child class, creating multiple levels.

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### Example Idea

A `Child` inherits from `Parent`, and `Parent` inherits from `Grandparent`.

---

## 2.4 Hierarchical Inheritance

In **hierarchical inheritance**, multiple child classes inherit from the same parent class.

```text
        Parent
       /      \
   Child 1   Child 2
```

### Example Idea

Both `Dog` and `Cat` can inherit from an `Animal` class.

---

## 2.5 Hybrid Inheritance

**Hybrid inheritance** is a combination of two or more types of inheritance.

It can combine structures such as multiple and multilevel inheritance.

```text
      Parent
      /    \
   Child   Child
      \    /
      Another
```

### Explanation

The exact structure depends on the types of inheritance being combined.

---

# 3. Access Specifiers in Python

Access specifiers are used to control how class attributes and methods are accessed.

Python commonly uses naming conventions to represent different levels of access.

### Public

A normal variable or method is considered public.

```python
name = "Student"
```

It can normally be accessed from outside the class.

---

### Protected

A single underscore `_` is commonly used to indicate a protected member.

```python
_name = "Student"
```

### Explanation

The single underscore is mainly a convention that tells programmers that the member is intended for internal use.

---

### Private

A double underscore `__` is used to indicate a private member.

```python
__name = "Student"
```

Python uses **name mangling** for double-underscore attributes, making direct access from outside the class more difficult.

---

# 4. Getters

A **getter** is a method used to access or retrieve the value of an attribute.

### Simple Idea

```text
Getter → Get the value
```

For example, a getter can be used to retrieve a private attribute.

---

# 5. Setters

A **setter** is a method used to change or update the value of an attribute.

### Simple Idea

```text
Setter → Set or change the value
```

A setter can also be used to validate a value before storing it.

---

# Key Learnings

* Learned what inheritance means.
* Learned about code reusability through inheritance.
* Learned Single Inheritance.
* Learned Multiple Inheritance.
* Learned Multilevel Inheritance.
* Learned Hierarchical Inheritance.
* Learned Hybrid Inheritance.
* Learned the basic idea of access specifiers.
* Understood public members.
* Understood protected members using `_`.
* Understood private members using `__`.
* Learned the purpose of getters.
* Learned the purpose of setters.

---

# Note

This day focuses on the **basic theory of inheritance and access control**. Practical coding examples of these concepts can be explored in the upcoming OOP practice days.
