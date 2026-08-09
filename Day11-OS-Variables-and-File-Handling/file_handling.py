# Day 11 - File Handling

# -----------------------------------
# Creating and Writing a File
# -----------------------------------

file = open("demo.txt", "w")               # Open file for writing

file.write("Hello Python\n")               # Write first line
file.write("Learning file handling")      # Write second line

file.close()                               # Close the file


# -----------------------------------
# Reading a File
# -----------------------------------

file = open("demo.txt", "r")               # Open file for reading

data = file.read()                         # Read complete file

print(data)                                # Display file content

file.close()                               # Close the file


# -----------------------------------
# Reading One Line
# -----------------------------------

file = open("demo.txt", "r")               # Open file for reading

line = file.readline()                     # Read one line

print(line)                                # Display the line

file.close()                               # Close the file


# -----------------------------------
# Reading Multiple Lines
# -----------------------------------

file = open("demo.txt", "r")               # Open file for reading

print(file.readline())                     # Read first line
print(file.readline())                     # Read second line

file.close()                               # Close the file


# -----------------------------------
# Appending to a File
# -----------------------------------

file = open("demo.txt", "a")               # Open file for append

file.write("\nNew content added.")        # Add new content

file.close()                               # Close the file


# -----------------------------------
# File Pointer - tell()
# -----------------------------------

file = open("demo.txt", "r")               # Open file for reading

print(file.tell())                         # Show pointer position

file.read(5)                               # Read five characters

print(file.tell())                         # Show new position

file.close()                               # Close the file


# -----------------------------------
# File Pointer - seek()
# -----------------------------------

file = open("demo.txt", "r")               # Open file for reading

file.seek(0)                               # Move pointer to start

print(file.read())                         # Read complete file

file.close()                               # Close the file


# -----------------------------------
# Truncate a File
# -----------------------------------

file = open("truncate.txt", "w")           # Open file for writing

file.write("Hello Python World")           # Write file content

file.truncate(5)                           # Keep first five characters

file.close()                               # Close the file


# -----------------------------------
# Reading Truncated File
# -----------------------------------

file = open("truncate.txt", "r")            # Open file for reading

print(file.read())                         # Display remaining content

file.close()                               # Close the file


# -----------------------------------
# Creating a New File
# -----------------------------------

try:
    file = open("new_file.txt", "x")       # Create new file

    file.close()                           # Close the file

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")


# -----------------------------------
# Text File Mode
# -----------------------------------

file = open("text_file.txt", "w")           # Open text file

file.write("This is text data.")           # Write text data

file.close()                               # Close the file


# -----------------------------------
# Binary File Mode
# -----------------------------------

file = open("binary_file.bin", "wb")        # Open binary file

file.write(b"Python")                      # Write binary data

file.close()                               # Close the file


# -----------------------------------
# Using with Statement
# -----------------------------------

with open("demo.txt", "r") as file:         # Open file safely

    print(file.read())                     # Read file content
