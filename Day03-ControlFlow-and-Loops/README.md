# Day 03 - Match Case Statements and Loops 🐍

## Introduction

On the third day of my Python learning journey, I learned how to control the flow of a program using **match-case statements**, **for loops**, and **while loops**. I also explored the `range()` function and learned how `break` and `continue` statements help control loop execution.

These concepts are essential for writing programs that can make decisions and perform repetitive tasks efficiently.

---

# 1. Match Case Statement

The **match-case** statement is used to compare a variable with different values and execute the matching block of code.

It is similar to the **switch-case statement** available in languages like **C++** and **Java**. Python introduced the `match-case` statement to make decision-making cleaner and easier when multiple conditions need to be checked.

### Example

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
```

### Output

```text
Tuesday
```

### Explanation

The value of `day` is `2`, so Python executes **case 2** and prints **Tuesday**.

---

# 2. For Loop

A **for loop** is used to repeat a block of code for a fixed number of times or to iterate through a sequence.

### Example

```python
for number in range(1, 6):
    print(number)
```

### Output

```text
1
2
3
4
5
```

### Explanation

The loop starts from **1** and prints numbers up to **5**.

---

# 3. The range() Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

### Parameters

* **start** → Starting value (included).
* **stop** → Ending value (not included).
* **step** → Increment value.

### Example

```python
for number in range(2, 11, 2):
    print(number)
```

### Output

```text
2
4
6
8
10
```

### Explanation

The loop starts from **2**, increases by **2**, and stops before **11**.

---

# 4. While Loop

A **while loop** repeatedly executes a block of code as long as the given condition is `True`.

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

### Explanation

The loop continues until the value of `count` becomes greater than **5**.

---

# 5. Break Statement

The `break` statement immediately stops the loop when a specific condition is met.

### Example

```python
for number in range(1, 6):
    if number == 4:
        break
    print(number)
```

### Output

```text
1
2
3
```

### Explanation

When the value becomes **4**, the loop stops immediately.

---

# 6. Continue Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

### Example

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

### Output

```text
1
2
4
5
```

### Explanation

The value **3** is skipped, and the loop continues with the remaining values.

---

## Key Learnings

* Learned how to use the `match-case` statement.
* Understood the purpose of `for` loops.
* Learned how the `range()` function works.
* Practiced writing `while` loops.
* Used `break` to stop a loop.
* Used `continue` to skip an iteration.
