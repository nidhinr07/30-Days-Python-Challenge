# Day 11 - OS Module, Variables and File Handling 🐍

## Introduction

On the eleventh day of my Python learning journey, I learned about the **OS Module**, **Local and Global Variables**, and **File Handling**. These concepts helped me understand how Python can work with files and folders, manage variables with different scopes, and read or write data to files.

---

# 1. OS Module

The `os` module provides functions for interacting with the operating system. It can be used to work with files, folders, directories, and paths.

## Common OS Functions

### os.listdir()

Returns the files and folders inside a directory.

```python
import os

print(os.listdir())
```

---

### os.getcwd()

Returns the current working directory.

```python
import os

print(os.getcwd())
```

---

### os.chdir()

Changes the current working directory.

```python
import os

os.chdir("folder_name")
```

---

### os.rename()

Renames a file or folder.

```python
import os

os.rename("old.txt", "new.txt")
```

---

### os.makedirs()

Creates a new directory, including parent directories if needed.

```python
import os

os.makedirs("folder1/folder2")
```

---

# 2. Local Variables

A **local variable** is created inside a function and can normally be accessed only within that function.

## Example

```python
def show_name():
    name = "Alex"
    print(name)

show_name()
```

### Explanation

The variable `name` is created inside the function, so it is a local variable.

---

# 3. Global Variables

A **global variable** is created outside a function and can be accessed from different parts of the program.

## Example

```python
name = "Alex"

def show_name():
    print(name)

show_name()
```

### Explanation

The variable `name` is created outside the function, so it can be accessed inside the function.

---

# 4. File Handling

File handling allows Python programs to create, read, write, and modify files.

The `open()` function is used to open a file.

## Syntax

```python
open("filename", "mode")
```

## Common File Modes

| Mode | Meaning |
|------|---------|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `x` | Create |
| `t` | Text |
| `b` | Binary |

---

# 5. Writing to a File

The `w` mode is used to write data to a file.

```python
file = open("demo.txt", "w")

file.write("Hello Python")

file.close()
```

### Explanation

The `write()` method writes data into the file.

---

# 6. Reading a File

The `r` mode is used to read data from a file.

```python
file = open("demo.txt", "r")

data = file.read()

print(data)

file.close()
```

### Explanation

The `read()` method reads the contents of the file.

---

# 7. Appending to a File

The `a` mode adds new data at the end of an existing file.

```python
file = open("demo.txt", "a")

file.write("\nNew line")

file.close()
```

### Explanation

Append mode keeps the existing data and adds new content at the end.

---

# 8. Creating a File

The `x` mode is used to create a new file.

```python
file = open("newfile.txt", "x")

file.close()
```

### Explanation

The file is created if it does not already exist.

---

# 9. Text and Binary Files

Python can work with text and binary data.

### Text Mode

```python
file = open("demo.txt", "rt")
```

### Binary Mode

```python
file = open("image.jpg", "rb")
```

`rt` means **read text**, while `rb` means **read binary**.

---

# 10. readline()

The `readline()` method reads one line from a file.

```python
file = open("demo.txt", "r")

print(file.readline())

file.close()
```

---

# 11. seek()

The `seek()` method changes the current position inside a file.

```python
file = open("demo.txt", "r")

file.seek(0)

print(file.read())

file.close()
```

### Explanation

`seek(0)` moves the file pointer back to the beginning.

---

# 12. tell()

The `tell()` method returns the current position of the file pointer.

```python
file = open("demo.txt", "r")

print(file.tell())

file.close()
```

---

# 13. truncate()

The `truncate()` method removes content from a file after a specified position.

```python
file = open("demo.txt", "w")

file.write("Hello Python")

file.truncate(5)

file.close()
```

### Explanation

Only the first five characters remain after truncating.

---

# Key Learnings

- Learned how to use the `os` module.
- Practiced working with directories and paths.
- Understood local and global variables.
- Learned how to create and open files.
- Practiced reading, writing, and appending files.
- Learned different file modes.
- Used `readline()`, `seek()`, `tell()`, and `truncate()`.
- Understood the difference between text and binary file modes.
