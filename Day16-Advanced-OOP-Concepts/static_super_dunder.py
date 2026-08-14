# Day 16 - Static Method, super(), and Dunder Methods


# -----------------------------------
# Static Method
# -----------------------------------

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b                     # Return sum of values


print(Calculator.add(10, 20))             # Call static method


# -----------------------------------
# super() Keyword
# -----------------------------------

class Parent:

    def show(self):
        print("Parent method")            # Display parent message


class Child(Parent):

    def show(self):
        super().show()                    # Call parent method
        print("Child method")             # Display child message


child = Child()                           # Create child object

child.show()                              # Call child method


# -----------------------------------
# __str__() Dunder Method
# -----------------------------------

class Student:

    def __init__(self, name):
        self.name = name                  # Store student name

    def __str__(self):
        return self.name                  # Return object text


student = Student("Alex")                 # Create student object

print(student)                            # Call __str__ method


# -----------------------------------
# __len__() Dunder Method
# -----------------------------------

class Team:

    def __init__(self, members):
        self.members = members            # Store team members

    def __len__(self):
        return len(self.members)          # Return member count


team = Team(["Alex", "Sam", "John"])      # Create team object

print(len(team))                          # Call __len__ method
