# Day 14 - Inheritance

# -----------------------------------
# Single Inheritance
# -----------------------------------

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()                              # Create child object

dog.eat()                                # Use parent method
dog.bark()                               # Use child method


# -----------------------------------
# Multiple Inheritance
# -----------------------------------

class Father:

    def skill_one(self):
        print("Father's skill")


class Mother:

    def skill_two(self):
        print("Mother's skill")


class Child(Father, Mother):

    def show(self):
        print("Child's method")


child = Child()                          # Create child object

child.skill_one()                        # Use father method
child.skill_two()                        # Use mother method
child.show()                             # Use child method


# -----------------------------------
# Multilevel Inheritance
# -----------------------------------

class Grandparent:

    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):

    def car(self):
        print("Parent's car")


class Son(Parent):

    def bike(self):
        print("Son's bike")


son = Son()                              # Create final object

son.house()                              # Use grandparent method
son.car()                                # Use parent method
son.bike()                               # Use child method


# -----------------------------------
# Hierarchical Inheritance
# -----------------------------------

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

car.start()                              # Use parent method
car.drive()                              # Use car method

bike.start()                             # Use parent method
bike.ride()                              # Use bike method


# -----------------------------------
# Hybrid Inheritance
# -----------------------------------

class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):

    def show_d(self):
        print("Class D")


d = D()                                  # Create object

d.show_a()                               # Use A method
d.show_b()                               # Use B method
d.show_c()                               # Use C method
d.show_d()                               # Use D method
