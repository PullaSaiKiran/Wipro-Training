#1. Write a program that asks the user for their age and checks if they are eligible to
#vote (18 years and older). Print a message based on their eligibility.

Age=int(input("Enter the Age : "))

if Age >= 18:
    print("Eligible To Vote... ")
else:
    print("Not Eligible To Vote...")