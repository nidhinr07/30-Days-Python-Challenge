# ------------------------------------------------------------
# Challenge: Student Information System
#
# Create a program that collects student details and demonstrates
# the Python concepts learned so far, including data types,
# string methods, conditional statements, loops, and functions.
# ------------------------------------------------------------


# Welcome function
def welcome(name):
    print(f"\nWelcome, {name}!")


# Result function
def check_result(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"


# Get student details
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
grade = input("Enter your grade (A/B/C): ").upper()


# Call welcome function
welcome(name)


print("\n========== Student Details ==========")

print("Name :", name)
print("Age :", age)
print("Marks :", marks)
print("Grade :", grade)


print("\n========== Data Types ==========")

print(type(name))
print(type(age))
print(type(marks))
print(type(grade))


print("\n========== String Methods ==========")

print("Length :", len(name))
print("Upper :", name.upper())
print("Lower :", name.lower())
print("Title :", name.title())
print("Replace :", name.replace("a", "@"))


print("\n========== Result ==========")

print(check_result(marks))


print("\n========== Grade ==========")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid Grade")


print("\n========== For Loop ==========")

for number in range(1, 6):
    print(number)


print("\n========== While Loop ==========")

count = 3

while count > 0:
    print(count)
    count -= 1


print("\n========== Break Statement ==========")

for number in range(1, 6):

    if number == 4:
        break

    print(number)


print("\n========== Continue Statement ==========")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)
