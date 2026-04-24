# Write a user-defined function factorial(n) that takes a positive integer n as an argument
# and returns its factorial. Use the function in a program and print the factorial of a given
# number.

def factorial(n):
    if n<0:
        return "Factorial is not defined with negative values"
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range( 2 , n+1):
            fact *=i
        return fact
num = int(input("Enter a  number :"))
print('factorial is :',factorial(num))
