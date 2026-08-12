# Day 14 - Access Modifiers

# -----------------------------------
# Public Member
# -----------------------------------

class Student:

    def __init__(self):
        self.name = "Student"              # Public variable

    def show_name(self):
        print(self.name)                   # Access public variable


student = Student()                        # Create object

print(student.name)                        # Access public variable
student.show_name()                        # Call public method


# -----------------------------------
# Protected Member
# -----------------------------------

class Employee:

    def __init__(self):
        self._salary = 25000                # Protected variable

    def show_salary(self):
        print(self._salary)                # Access protected variable


employee = Employee()                       # Create object

print(employee._salary)                    # Access protected variable
employee.show_salary()                     # Call method


# -----------------------------------
# Private Member
# -----------------------------------

class Bank:

    def __init__(self):
        self.__balance = 5000               # Private variable

    def show_balance(self):
        print(self.__balance)              # Access private variable


bank = Bank()                              # Create object

bank.show_balance()                        # Access through method
