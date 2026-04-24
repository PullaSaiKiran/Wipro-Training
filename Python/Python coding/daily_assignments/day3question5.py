# Combining Built-in and User-Defined Functions:
# Find the Average of a List:
# Write a user-defined function average(numbers) that takes a list of numbers as an
# argument and returns the average of the numbers. Call the function with a list of
# numbers and print the average.


def average(numbers):
    if len(numbers) == 0:
        return "List is empty, cannot calculate average"
    return sum(numbers) / len(numbers)

nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("The average is:", average(nums))
