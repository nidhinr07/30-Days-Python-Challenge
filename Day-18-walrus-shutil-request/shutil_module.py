# Day 18 - Shutil Module

import shutil
import os


# -----------------------------------
# Copy a File
# -----------------------------------

shutil.copy("source.txt", "backup.txt")     # Copy file to new location

print("File copied successfully")           # Display success message


# -----------------------------------
# Move a File
# -----------------------------------

shutil.move("backup.txt", "new_backup.txt") # Move file to new location

print("File moved successfully")            # Display success message


# -----------------------------------
# Create Directory
# -----------------------------------

os.makedirs("demo_folder", exist_ok=True)   # Create folder if missing


# -----------------------------------
# Copy Directory
# -----------------------------------

shutil.copytree(
    "demo_folder",
    "demo_copy",
    dirs_exist_ok=True
)                                           # Copy complete directory


# -----------------------------------
# Remove Directory
# -----------------------------------

shutil.rmtree("demo_copy")                  # Remove complete directory

print("Directory removed successfully")     # Display success message
