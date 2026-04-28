# Use the Random Module:
# Write a program that imports the random module and uses it to:
# Generate and print a random integer between 1 and 100.
# Create a list of random numbers  and print the list.
# Shuffle a list of numbers and print the shuffled list.

import random

# Generate and print a random integer between 1 and 100
rand_int = random.randint(1, 100)
print("Random integer between 1 and 100:", rand_int)

# Create a list of random numbers and print the list
random_list = [random.randint(1, 100) for _ in range(10)]  # 10 random numbers
print("List of random numbers:", random_list)

# Shuffle a list of numbers and print the shuffled list
numbers = list(range(1, 11))  # numbers from 1 to 10
print("Original list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)
