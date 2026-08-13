# Question 01 - Student Class
# Create a student class and display details.


class Student:

    def __init__(self, name, age):
        self.name = name                 # Store student name
        self.age = age                   # Store student age

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


student = Student("Alex", 20)            # Create student object

student.show_details()                   # Display student details
