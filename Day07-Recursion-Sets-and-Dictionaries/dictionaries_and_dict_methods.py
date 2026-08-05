# Day 07 - Dictionaries and Dictionary Methods

# -----------------------------------
# Creating a Dictionary
# -----------------------------------

student = {
    "name": "Alex",
    "age": 20,
    "course": "Python"
}                                         # Create dictionary

print(student)                            # Display dictionary


# -----------------------------------
# Accessing Dictionary Values
# -----------------------------------

print(student["name"])                    # Access using key
print(student.get("course"))              # Access using get()


# -----------------------------------
# Updating Dictionary
# -----------------------------------

student["age"] = 21                       # Update value

print(student)


# -----------------------------------
# Adding New Key-Value Pair
# -----------------------------------

student["city"] = "Chennai"               # Add new item

print(student)


# -----------------------------------
# Dictionary Methods
# -----------------------------------

print(student.keys())                     # Display all keys

print(student.values())                   # Display all values

print(student.items())                    # Display key-value pairs


# -----------------------------------
# Update Method
# -----------------------------------

student.update({"course": "Full Stack"})  # Update dictionary

print(student)


# -----------------------------------
# Pop Method
# -----------------------------------

student.pop("city")                       # Remove key

print(student)


# -----------------------------------
# Popitem Method
# -----------------------------------

student.popitem()                         # Remove last item

print(student)


# -----------------------------------
# Clear Method
# -----------------------------------

temp = {
    "a": 10,
    "b": 20
}                                         # Temporary dictionary

temp.clear()                              # Remove all items

print(temp)
