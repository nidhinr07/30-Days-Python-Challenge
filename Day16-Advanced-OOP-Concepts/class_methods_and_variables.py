# Day 16 - Class Methods and Variables


# -----------------------------------
# Instance Variables
# -----------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name                  # Store object name
        self.age = age                    # Store object age


student1 = Student("Alex", 20)            # Create first object
student2 = Student("Sam", 21)             # Create second object

print(student1.name)
print(student2.name)


# -----------------------------------
# Class Variable
# -----------------------------------

class StudentInfo:

    school = "Python School"              # Class variable

    def __init__(self, name):
        self.name = name                  # Instance variable


student1 = StudentInfo("Alex")            # Create first object
student2 = StudentInfo("Sam")             # Create second object

print(student1.name)
print(student2.name)

print(student1.school)                   # Access class variable
print(student2.school)                   # Access class variable


# -----------------------------------
# Class Method
# -----------------------------------

class School:

    school_name = "Python School"         # Class variable

    @classmethod
    def show_school(cls):
        print(cls.school_name)            # Access class variable


School.show_school()                      # Call class method


# -----------------------------------
# Alternative Constructor
# -----------------------------------

class StudentData:

    def __init__(self, name, age):
        self.name = name                  # Store student name
        self.age = age                    # Store student age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")       # Split string values
        return cls(name, int(age))        # Create object


student = StudentData.from_string("Alex-20")

print(student.name)
print(student.age)


# -----------------------------------
# dir()
# -----------------------------------

numbers = [1, 2, 3]                       # Create list

print(dir(numbers))                       # Show available methods


# -----------------------------------
# __dict__
# -----------------------------------

print(student.__dict__)                   # Show object attributes


# -----------------------------------
# help()
# -----------------------------------

help(str.upper)                           # Show method information
