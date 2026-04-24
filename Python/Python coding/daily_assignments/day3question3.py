# Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
# arguments and returns the largest of the three. Use the function in a program to find and
# print the largest of three given numbers.

def find_largest(a, b, c):
    largest = a

    if b > largest:
        largest = b
    if c > largest:
        largest = c

    return largest

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

print("The largest number is:", find_largest(n1, n2, n3))
