# Write a program that takes a password as input and checks if it is strong (at least
# 8 characters). Print a message based on the result.

Password = input("Enter the Password : ")
p=len(Password)

if p==8:
    print("Password is Strong")
else:
    print("Password is Not strong")