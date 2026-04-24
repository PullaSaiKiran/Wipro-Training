# Write a user-defined function greet(name) that takes a name as an argument and prints
# a greeting message like "Hello, [name]!" Use the function to greet the user with their
# name.


def greet(name):
    print(f"Hello, {name}!")

username = input("Enter your name: ")
greet(username)
