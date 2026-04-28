# Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and
# string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to
# uppercase, and finding the length of a string.
# In string_validations.py, define functions to check if a string is a palindrome and if it
# contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package.


# main.py
from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_validations import is_palindrome, is_alpha

# String operations
text = "HelloWorld"
print("Original String:", text)
print("Reversed String:", reverse_string(text))
print("Uppercase String:", to_uppercase(text))
print("Length of String:", string_length(text))

# String validations
pal_text = "madam"
alpha_text = "Python"

print(f"Is '{pal_text}' a palindrome?", is_palindrome(pal_text))
print(f"Does '{alpha_text}' contain only alphabets?", is_alpha(alpha_text))

