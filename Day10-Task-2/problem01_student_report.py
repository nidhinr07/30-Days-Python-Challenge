# Create a student report using basic Python concepts.
# Store students, calculate results, and handle invalid input.

students = []                              # Store student details


def check_result(marks):
    if marks >= 50:                        # Check passing marks
        return "Pass"
    else:
        return "Fail"


while True:
    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter student age: "))
        marks = int(input("Enter student marks: "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

    except ValueError as error:
        print("Invalid input:", error)
        continue

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "result": check_result(marks)
    }

    students.append(student)

    choice = input("Add another student? (yes/no): ").lower()

    if choice != "yes":
        break


print("\n---------- Student Report ----------")

for student in students:
    print(f"Name   : {student['name']}")
    print(f"Age    : {student['age']}")
    print(f"Marks  : {student['marks']}")
    print(f"Result : {student['result']}")
    print()
