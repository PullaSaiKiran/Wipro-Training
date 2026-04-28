# Use the Math Module:
# Write a program that imports the math module and uses it to:
# Find the square root of a number.
# Calculate the sine of an angle .
# Find the greatest common divisor (GCD) of two numbers .

import math

n=int(input("enter the number"))
print("Square root of a number :",math.sqrt(n))

angle=int(input("Enter the angle : "))
print("Sine of", angle, "degrees is:", math.sin(math.radians(angle)))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD of", a, "and", b, "is:", math.gcd(a, b))