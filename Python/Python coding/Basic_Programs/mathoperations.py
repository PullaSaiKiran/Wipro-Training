from Mypack.basicshapes import areaoftrianle,areaofsquare,perimeterofsquare
from Mypack.circle import areaofcircle, perimeterofcircle

radius = int(input("Enter Radius : "))

print('Area:',areaofcircle(rad=radius))
print('perimeter:',perimeterofcircle(rad=radius))

s=int(input('enter the side'))
print('Area of square ', areaofsquare(side=s))
print('Perimeter of square',perimeterofsquare(side=s))


l = int(input("Enter length"))
b= int(input("Enter Breadth"))
print('Area:', areaoftrianle(l,b))