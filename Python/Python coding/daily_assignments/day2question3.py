# Do the following in sequence and record the results in a single program
# Create a set of 5 unique colors. Print the set.
# Add a new color to the set, then try removing an existing color. Print the updated set.
# Create another set with 3 different colors. Find the intersection, union, and difference
# between both sets.
# Check if a specific color is in the set and print the result.
# Convert a list of fruits (with some duplicates) into a set and print the unique fruits.

s1={'Red' , 'Yellow', 'Green' , 'Blue' , 'Orange'}
print('Colors:',s1)

s1.add('Black')
print('Added:',s1)

s1.remove('Red')
print('Remove:',s1)

s2={'Purple','Blue','White','NavyBlue'}
print('New Set :',s2)


print('Intersection :',s1.intersection(s2))

print('Union :',s1.union(s2))

print('Differnce :',s1.difference(s2))

print('Check Blue in Colors ?',"Blue" in s1)

print('Check Black in Colors ?',"Black" in s2)


fruits_list = ["Apple", "Banana", "Apple", "Orange", "Banana", "Mango"]
unique_fruits = set(fruits_list)
print("Unique fruits:", unique_fruits)