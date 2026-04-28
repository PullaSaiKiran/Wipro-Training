from oopconcepts.rectangle import Rectangle
from oopconcepts.square import  Square

sqobj = Square(10)


print(f'Area:{sqobj.calculate_area()}\t perimeter :{sqobj.calculate_perimeter}')
rectobj=Rectangle(10,5)
print(f'Area:{rectobj.calculate_area()}\t perimeter :{rectobj.calculate_perimeter}')
