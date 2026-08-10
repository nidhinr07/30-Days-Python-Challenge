# Day 12 - == and is Operators


# -----------------------------------
# == Operator
# -----------------------------------

a = 10                                      # Store first value
b = 10                                      # Store second value

print(a == b)                               # Compare both values


# -----------------------------------
# Different Values
# -----------------------------------

x = 10                                      # Store first value
y = 20                                      # Store second value

print(x == y)                               # Compare both values


# -----------------------------------
# is Operator
# -----------------------------------

list1 = [1, 2, 3]                           # Create first list
list2 = list1                               # Same object reference

print(list1 is list2)                       # Check same object


# -----------------------------------
# Different Objects
# -----------------------------------

list1 = [1, 2, 3]                           # Create first list
list2 = [1, 2, 3]                           # Create second list

print(list1 == list2)                       # Compare list values
print(list1 is list2)                       # Compare object identity


# -----------------------------------
# == and is Together
# -----------------------------------

a = [10, 20]                                # Create first list
b = a                                       # Reference same object

print(a == b)                               # Check equal values
print(a is b)                               # Check same object


# -----------------------------------
# None with is
# -----------------------------------

value = None                                # Store None value

print(value is None)                        # Check for None
