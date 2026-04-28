# Write a program that asks the user to enter some text and saves it to a file called
# output.txt. Then, open the file and read its contents, printing them to the console.

# def write_to_file(filename):
#     # Ask the user for input
#     text = input("Enter some text: ")
#
#     # Write the text to the file
#     with open(filename, "w") as file:
#         file.write(text)
#     print(f"Text written to {filename} successfully.")
#
#
# def read_from_file(filename):
#     # Read the contents of the file
#     with open(filename, "r") as file:
#         contents = file.read()
#     print("Contents of the file:")
#     print(contents)
#
#
# # Main program
# filename = "output.txt"
# write_to_file(filename)
# read_from_file(filename)

# Write a program that reads a text file called sample.txt and counts the number of lines,
# words, and characters in the file. Print the counts.
# def count_file_stats(filename):
#     with open(filename, "r") as file:
#         text = file.read()
#
#         # Count lines
#         lines = text.splitlines()
#         num_lines = len(lines)
#
#         # Count words
#         words = text.split()
#         num_words = len(words)
#
#         # Count characters
#         num_chars = len(text)
#
#         print(f"Lines: {num_lines}")
#         print(f"Words: {num_words}")
#         print(f"Characters: {num_chars}")
#
#
# # Main program
# filename = "output.txt"
# count_file_stats(filename)

# Write a program that reads the contents of a file called source.txt and writes the
# contents to another file called destination.txt. Ensure that destination.txt is created if it
# doesn't exist.
# def copy_file(source, destination):
#     # Open source file in read mode
#     with open(source, "r") as src:
#         contents = src.read()
#
#     # Open destination file in write mode (creates file if it doesn't exist)
#     with open(destination, "w") as dest:
#         dest.write(contents)
#
#     print(f"Contents copied from {source} to {destination} successfully.")
#
#
# # Main program
# source_file = "output.txt"
# destination_file = "destination.txt"
# copy_file(source_file, destination_file)

# Write a program that appends a line of text to a file called log.txt. After appending the
# text, open the file and print its contents to verify that the text was added.

# def append_to_log(filename):
#     # Ask the user for a line of text
#     text = input("Enter a line of text to append: ")
#
#     # Open the file in append mode (creates file if it doesn't exist)
#     with open(filename, "a") as file:
#         file.write(text + "\n")
#     print(f"Text appended to {filename} successfully.")
#
#
# def read_log(filename):
#     # Read and print the contents of the file
#     with open(filename, "r") as file:
#         contents = file.read()
#     print("Contents of the log file:")
#     print(contents)
#
#
# # Main program
# filename = "output.txt"
# append_to_log(filename)
# read_log(filename)

# Write a program that asks the user to input a number in the form of a string. Use a try
# except block to convert the string to an integer. If a ValueError occurs (e.g., if the user
# inputs a non-numeric string), print an error message. Otherwise, print the integer.

# def convert_to_int():
#     # Ask the user for input
#     user_input = input("Enter a number: ")
#
#     try:
#         # Try converting to integer
#         number = int(user_input)
#         print(f"You entered the integer: {number}")
#     except ValueError:
#         # Handle non-numeric input
#         print("Error: That is not a valid integer.")
#
#
# # Main program
# convert_to_int()

# Write a program that tries to open a file specified by the user for reading. Use a try
# except block to handle FileNotFoundError if the file does not exist. If the file is
# successfully opened, print its contents; otherwise, print an error message.

# def read_file():
#     # Ask the user for the filename
#     filename = input("Enter the filename to open: ")
#
#     try:
#         # Try to open and read the file
#         with open(filename, "r") as file:
#             contents = file.read()
#         print("File contents:")
#         print(contents)
#     except FileNotFoundError:
#         # Handle the case where the file does not exist
#         print(f"Error: The file '{filename}' was not found.")
#
#
# # Main program
# read_file()

# Write a program that asks the user to input two numbers and performs division. Use a
# try-except block to handle both ZeroDivisionError and ValueError. Print different
# messages for each exception. If no exception occurs, print the result of the division.

# def divide_numbers():
#     try:
#         # Ask the user for two numbers
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#
#         # Perform division
#         result = num1 / num2
#         print(f"Result of division: {result}")
#
#     except ZeroDivisionError:
#         # Handle division by zero
#         print("Error: Division by zero is not allowed.")
#
#     except ValueError:
#         # Handle invalid input (non-numeric)
#         print("Error: Please enter valid integers.")
#
#
# # Main program
# divide_numbers()

# Write a program that takes a list of numbers and asks the user to input an index to
# access an element from the list. Use a try-except block to handle IndexError if the user
# enters an invalid index. Print the corresponding element if the index is valid; otherwise,
# print an error message.

# def access_element():
#     # Example list of numbers
#     numbers = [10, 20, 30, 40, 50]
#     print("Numbers list:", numbers)
#
#     try:
#         # Ask the user for an index
#         index = int(input("Enter an index to access: "))
#
#         # Access the element at the given index
#         element = numbers[index]
#         print(f"Element at index {index}: {element}")
#
#     except IndexError:
#         # Handle invalid index
#         print("Error: Invalid index. Please enter a valid index within the list range.")
#
#     except ValueError:
#         # Handle non-numeric input
#         print("Error: Please enter a valid integer index.")
#
#
# # Main program
# access_element()
# Write a program that defines a custom exception class NegativeNumberError. The
# program should ask the user to input a positive number. If the user enters a negative
# number, raise the NegativeNumberError and handle it using a try-except block, printing
# an appropriate error message.

# # Define custom exception class
# class NegativeNumberError(Exception):
#     pass
#
#
# def get_positive_number():
#     try:
#         # Ask the user for input
#         num = int(input("Enter a positive number: "))
#
#         # Check if the number is negative
#         if num < 0:
#             raise NegativeNumberError("Negative number entered.")
#
#         print(f"You entered: {num}")
#
#     except NegativeNumberError as e:
#         print(f"Error: {e}")
#
#     except ValueError:
#         print("Error: Please enter a valid integer.")
#
#
# # Main program
# get_positive_number()

# Write a program that repeatedly asks the user to input two numbers and performs
# division. Use a try-except block inside a loop to handle ZeroDivisionError and
# ValueError. The program should continue until the user provides valid input and a valid
# division result is printed.
#
# def divide_until_valid():
#     while True:  # Keep looping until valid division
#         try:
#             # Ask the user for two numbers
#             num1 = int(input("Enter the first number: "))
#             num2 = int(input("Enter the second number: "))
#
#             # Perform division
#             result = num1 / num2
#             print(f"Result of division: {result}")
#             break  # Exit loop once successful
#
#         except ZeroDivisionError:
#             print("Error: Division by zero is not allowed. Please try again.")
#
#         except ValueError:
#             print("Error: Please enter valid integers. Try again.")
#
#
# # Main program
# divide_until_valid()

# Write a program that tries to open and read a file. Use a try-except-finally block to
# handle potential exceptions like FileNotFoundError. Ensure that the finally block prints a
# message indicating that the program has completed, whether an exception occurred or
# not.
#
# def read_file(filename):
#     try:
#         # Try to open and read the file
#         with open(filename, "r") as file:
#             contents = file.read()
#         print("File contents:")
#         print(contents)
#
#     except FileNotFoundError:
#         # Handle case where file does not exist
#         print(f"Error: The file '{filename}' was not found.")
#
#     finally:
#         # This block always executes
#         print("Program has completed execution.")
#
#
# # Main program
# filename = "output.txt"  # You can change this to any file name
# read_file(filename)

# Write a program that defines a function to add two numbers. Use a try-except block to
# handle TypeError in case the function is called with non-numeric arguments (e.g.,
# strings). Print an appropriate error message if the exception is caught.
#
#
# # Define a function to add two numbers
# def add_numbers(a, b):
#     try:
#         result = a + b
#         print(f"Result: {result}")
#     except TypeError:
#         print("Error: Both arguments must be numbers.")
#
# # Main program
# # Valid call
# add_numbers(10, 20)
#
# # Invalid call (string + int)
# add_numbers("hello", 5)



# Write a program that repeatedly asks the user to input an integer. Use a `try-except`
# block to handle `ValueError` in case the user enters a non-integer value. The program
# should keep asking for input until a valid integer is provided, and then print the integer.


def get_integer():
    while True:  # Keep looping until valid input
        try:
            num = int(input("Enter an integer: "))
            print(f"You entered: {num}")
            break  # Exit loop once a valid integer is entered
        except ValueError:
            print("Error: Please enter a valid integer.")

# Main program
get_integer()
