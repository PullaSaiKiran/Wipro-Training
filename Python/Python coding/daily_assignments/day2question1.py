# Do the following in sequence and record the results in a single program
# Create a list with 5 different types of fruits. Print the list.
# Add two more fruits to the list, then remove one fruit from it. Print the updated list.
# Access the second and fourth fruits in the list. Print them.
# Slice the list to get the first three fruits and print the result.
# Find and print the length of your list.

fruits = ['Apple' , 'Banana' , 'Grapes' , 'Pomegranate' , 'Pineapple']
print(fruits)

fruits.append('Kiwi')
fruits.append('Dragon Fruit')
print(fruits)

fruits.remove('Grapes')
print(fruits)


print('second',[fruits[2]] )
print('fourth',[fruits[4]])


i=fruits[:3:]
print(i)

l=len(fruits)
print('count',l)