# Day 17 - Method Overriding


# Parent class with method
class Animal:

    def sound(self):
        print("Animal makes sound")          # Display animal sound


# Child class overrides method
class Dog(Animal):

    def sound(self):
        print("Dog barks")                    # Override parent method


animal = Animal()                             # Create animal object
dog = Dog()                                   # Create dog object

animal.sound()                                # Call parent method
dog.sound()                                   # Call child method


# Another overriding example
class Vehicle:

    def start(self):
        print("Vehicle is starting")          # Display vehicle message


class Car(Vehicle):

    def start(self):
        print("Car is starting")              # Override vehicle method


vehicle = Vehicle()                           # Create vehicle object
car = Car()                                   # Create car object

vehicle.start()                               # Call parent method
car.start()                                   # Call child method
