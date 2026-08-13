# Question 03 - Vehicle Inheritance
# Create child classes from a vehicle class.


class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")


car = Car()                              # Create car object
bike = Bike()                            # Create bike object

car.start()                              # Use inherited method
car.drive()                              # Use car method

bike.start()                             # Use inherited method
bike.ride()                              # Use bike method
