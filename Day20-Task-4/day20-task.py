
## `day20_task.py`

```python
# Day 20 - Student Performance Analyzer
# Practice task combining concepts learned so far


# Create tuple of subjects
subjects = ("Math", "Python", "English", "Database", "Computer")


# Get student name
name = input("Enter student name: ")


# Store marks in a list
marks = []


# Get marks with exception handling
for subject in subjects:

    while True:

        try:
            mark = int(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break

            print("Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Function to calculate total
def calculate_total(mark_list):

    return sum(mark_list)


# Function to calculate average
def calculate_average(mark_list):

    return sum(mark_list) / len(mark_list)


# Calculate total and average
total = calculate_total(marks)
average = calculate_average(marks)


# Determine result
if average >= 90:
    result = "Excellent"

elif average >= 75:
    result = "Very Good"

elif average >= 50:
    result = "Pass"

else:
    result = "Fail"


# List comprehension for passed marks
passed_marks = [mark for mark in marks if mark >= 50]


# Set for unique marks
unique_marks = set(marks)


# Store student information
student = {
    "name": name,
    "marks": marks,
    "total": total,
    "average": average,
    "result": result
}


# Generator function
def generate_marks(mark_list):

    for mark in mark_list:
        yield mark


# Create generator
mark_generator = generate_marks(marks)


# Display report
print("\n----- Student Report -----")

print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", student["total"])
print("Average:", student["average"])
print("Result:", student["result"])

print("Passed Marks:", passed_marks)
print("Unique Marks:", unique_marks)

print("Subjects:", subjects)

print("\nMarks using Generator:")

for mark in mark_generator:
    print(mark)
