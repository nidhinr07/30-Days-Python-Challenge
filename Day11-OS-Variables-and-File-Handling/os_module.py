# Day 11 - OS Module

import os

# -----------------------------------
# Current Working Directory
# -----------------------------------

print(os.getcwd())                         # Show current folder


# -----------------------------------
# List Files and Folders
# -----------------------------------

print(os.listdir())                        # Show folder contents


# -----------------------------------
# Create a Directory
# -----------------------------------

if not os.path.exists("demo_folder"):
    os.makedirs("demo_folder")             # Create new folder

print("Folder created.")


# -----------------------------------
# Change Directory
# -----------------------------------

current_folder = os.getcwd()              # Save current folder

os.chdir("demo_folder")                    # Change current folder

print(os.getcwd())                         # Show new folder


# -----------------------------------
# Change Back Directory
# -----------------------------------

os.chdir(current_folder)                   # Return to old folder

print(os.getcwd())                         # Show current folder


# -----------------------------------
# Rename a File
# -----------------------------------

if os.path.exists("old_name.txt"):
    os.rename("old_name.txt", "new_name.txt")  # Rename file

    print("File renamed.")


# -----------------------------------
# Check Path
# -----------------------------------

print(os.path.exists("demo_folder"))       # Check path exists

print(os.path.isfile("demo_folder"))      # Check if file

print(os.path.isdir("demo_folder"))       # Check if folder
