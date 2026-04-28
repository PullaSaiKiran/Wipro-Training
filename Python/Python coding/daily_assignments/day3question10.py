# Use the OS Module:
# Write a program that imports the os module and uses it to:
# Print the current working directory
# Create a new directory and verify its existence.
# List all files and directories in the current directory


import os

# 1. Print the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# 2. Create a new directory
new_dirrectory = "My_mathh"
os.mkdir(new_dirrectory)
print(f"Directory '{new_dirrectory}' created successfully.")

# 3. Verify its existence
if os.path.exists(new_dirrectory):
    print(f"Verified: '{new_dirrectory}' exists in the current directory.")

# 4. List all files and directories in the current directory
items = os.listdir(current_directory)
print("Files and Directories in Current Directory:")
for item in items:
    print(item)
