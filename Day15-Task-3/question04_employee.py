# Question 04 - Employee Management
# Use inheritance with private salary.


class Employee:

    def __init__(self, name, age, salary):
        self.name = name                  # Store employee name
        self.age = age                    # Store employee age
        self.__salary = salary            # Store private salary

    def get_salary(self):
        return self.__salary              # Return salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary        # Update valid salary

    def show_details(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Salary : {self.get_salary()}")


class Developer(Employee):

    def show_role(self):
        print("Role   : Developer")


class Manager(Employee):

    def show_role(self):
        print("Role   : Manager")


developer = Developer("Alex", 22, 30000)  # Create developer
manager = Manager("Sam", 25, 45000)      # Create manager

developer.show_details()
developer.show_role()

print()

manager.show_details()
manager.show_role()

developer.set_salary(35000)              # Update developer salary

print("\nUpdated Salary:", developer.get_salary())
