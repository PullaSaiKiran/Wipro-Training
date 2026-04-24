# Do the following in sequence and record the results in a single program
# Create a tuple with the names of 3 different cities you’d like to visit. Print the tuple.:
# Access and print the first and last elements of the tuple.:
# Create another tuple with 2 more cities. Concatenate both tuples and print the result.
# Try changing one element of the tuple. What happens?
# Unpack the elements of the tuple into separate variables and print them
from daily_assignments.q2 import index

tup = ('Hyderabad' , 'Pune' , 'Chennai')
print('Cities',tup)

print('First Tuple :',tup[0])
print('Last Tuple :',tup[2])

tup2=('Mumbai', 'Delhi')
print(tup2)

Merge = (tup+tup2)
print(Merge)


# tup[0]='Kolkata'
# print(tup)  #error because tuple is immutable

tup = ('Hyderabad' , 'Pune' , 'Chennai')

city1, city2, city3 = tup

print(city1)
print(city2)
print(city3)