# Day 22 - Student Marks


students = {
    "Alex": 85,
    "Sam": 92,
    "John": 76,
    "David": 88
}


print("----- Student Marks -----")

for name, marks in students.items():
    print(name, ":", marks)


highest = max(students.values())

average = sum(students.values()) / len(students)


print("\nHighest Mark:", highest)
print("Average Mark:", average)
