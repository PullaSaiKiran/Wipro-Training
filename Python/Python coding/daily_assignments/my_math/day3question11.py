# Create and Use a Custom Package:
# Create a package called my_math with two modules: arithmetic.py and geometry.py.
# In arithmetic.py, define functions for addition, subtraction, multiplication, and division.
# In geometry.py, define functions to calculate the area of a circle and the area of a
# rectangle.
# Write a program that imports these functions from the my_math package and uses
# them to perform various calculations.

# main.py
from my_math.arithmetic import add, subtract, multiply, divide
from my_math.geometry import area_circle, area_rectangle

# Arithmetic operations
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# Geometry calculations
print("Area of Circle (radius=7):", area_circle(7))
print("Area of Rectangle (length=10, width=5):", area_rectangle(10, 5))
