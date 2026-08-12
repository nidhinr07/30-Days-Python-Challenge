# Day 14 - Getters and Setters


# -----------------------------------
# Getter and Setter
# -----------------------------------

class Student:

    def __init__(self, name, age):
        self.__name = name                  # Store private name
        self.__age = age                    # Store private age

    # Getter for name
    def get_name(self):
        return self.__name                  # Return private name

    # Setter for name
    def set_name(self, name):
        self.__name = name                  # Update private name

    # Getter for age
    def get_age(self):
        return self.__age                   # Return private age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age                # Update valid age
        else:
            print("Age must be positive.")


# -----------------------------------
# Creating Object
# -----------------------------------

student = Student("Student", 20)            # Create object


# -----------------------------------
# Using Getters
# -----------------------------------

print(student.get_name())                   # Get student name
print(student.get_age())                    # Get student age


# -----------------------------------
# Using Setters
# -----------------------------------

student.set_name("Python Student")          # Change student name
student.set_age(21)                         # Change student age


# -----------------------------------
# Display Updated Values
# -----------------------------------

print(student.get_name())                   # Show updated name
print(student.get_age())                    # Show updated age
