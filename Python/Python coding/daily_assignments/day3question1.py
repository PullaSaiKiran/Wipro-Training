# Do the following in a single program using built-in functions
# Take a list of numbers as input and print the largest and smallest numbers in the list.
# Take a string as input and print the length of the string.
# Take a list of names as input and print the list in alphabetical order.
# Take a list of numbers as input and print the total sum of the elements in the list.
# Takes a string as input and print the string in uppercase.


numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

text = input("Enter a string: ")
print("Length of string:", len(text))


names = input("Enter names separated by space: ").split()
print("Names in alphabetical order:", sorted(names))


nums = [int(x) for x in input("Enter the numbers with separated by space").split()]
print("Sum of numbers:", sum(nums))


string_input = input("Enter a string: ")
print("Uppercase string:", string_input.upper())

