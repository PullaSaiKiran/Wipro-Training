# Do the following in sequence and record the results in a single program
# Create a dictionary with your name, age, and favorite hobby as keys, and provide
# appropriate values. Print the dictionary.
# Access and print the value associated with your name in the dictionary.
# Add a new key-value pair for your favorite food, then update the value for your favorite
# hobby. Print the updated dictionary.
# Print all the keys and all the values in the dictionary separately.
# Remove the age key-value pair from the dictionary. Print the dictionary to see the
# change.

dict_sample = { 'name' : 'Saikiran', 'age' : '22' ,'favorite hobby':'Reading Books' }
print(dict_sample)

print('name :',dict_sample['name'])

dict_sample['food']='Biryani'
print(dict_sample)
dict_sample['favorite hobby']='Playing Games'

print(dict_sample.pop('age'))

print('Updated Dictionary',dict_sample)
