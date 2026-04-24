# 11. Write a program that uses a for loop to count the number of vowels in a given
# string. Print the count.



text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"Number of vowels in the string:",count)
