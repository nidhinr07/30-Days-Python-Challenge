# Day 20 - Python Practice Challenge 🧩

## Introduction

After learning different Python concepts during the previous days, I completed a practice challenge that combines several concepts together.

This challenge focuses on using Python concepts together to build a simple **Student Performance Analyzer**.

---

# Challenge

## Student Performance Analyzer

Create a Python program that manages and analyzes the marks of a student.

The program should perform the following tasks:

1. Ask the user to enter the student's name.

2. Ask the user to enter marks for 5 subjects.

3. Store all the marks in a list.

4. Store the subject names in a tuple.

5. Create a function to calculate the total marks.

6. Create another function to calculate the average marks.

7. Use `if-elif-else` to determine the student's result:

   - Average >= 90 → Excellent
   - Average >= 75 → Very Good
   - Average >= 50 → Pass
   - Below 50 → Fail

8. Use list comprehension to create a list containing only the marks that are 50 or above.

9. Use a set to display the unique marks.

10. Store the student's information in a dictionary.

11. Use exception handling to handle invalid mark input.

12. Create a generator function that generates the marks one by one.

13. Display a final student report containing the student's name, marks, total, average, and result.

---

# Example Output

```text
Enter student name: Alex

Enter marks:
Math: 85
Python: 92
English: 76
Database: 88
Computer: 95

----- Student Report -----

Name: Alex
Marks: [85, 92, 76, 88, 95]

Total: 436
Average: 87.2
Result: Very Good

Passed Marks: [85, 92, 76, 88, 95]

Unique Marks: {85, 92, 76, 88, 95}

Subjects:
('Math', 'Python', 'English', 'Database', 'Computer')
