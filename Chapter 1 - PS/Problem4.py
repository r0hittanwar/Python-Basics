# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

# specify the directory path
path = input("Enter directory path: ")

try:
    # get list of all files and directories
    contents = os.listdir(path)

    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access this directory.")
