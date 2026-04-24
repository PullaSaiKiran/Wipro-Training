# Write a program that takes a number as input and checks if it is divisible by 5.
# Print a message if it is divisible or not.

Num = int(input("Enter the Number : "))
if Num % 5 == 0:
    print(Num," is Divisible by 5")
else:
    print(Num," is Not Divisible by 5")