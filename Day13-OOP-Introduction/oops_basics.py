# Day 13 - OOP Basics

# -----------------------------------
# Creating a Class
# -----------------------------------

class Student:

    # Default Constructor
    def __init__(self):
        self.name = "Student"              # Store default name
        self.age = 20                      # Store default age

    # Display student details
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# -----------------------------------
# Creating an Object
# -----------------------------------

student1 = Student()                       # Create object

student1.show_details()                    # Display details


# -----------------------------------
# Parameterized Constructor
# -----------------------------------

class StudentInfo:

    def __init__(self, name, age):
        self.name = name                   # Store student name
        self.age = age                     # Store student age

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# -----------------------------------
# Creating Objects
# -----------------------------------

student1 = StudentInfo("Alex", 20)         # Create first object
student2 = StudentInfo("Sam", 21)          # Create second object

student1.show_details()                    # Show first student
student2.show_details()                    # Show second student
