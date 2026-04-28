# Check Palindrome:
# Write a user-defined function is_palindrome(s) that takes a string as an argument and
# returns True if the string is a palindrome (reads the same forward and backward), and
# False otherwise. Test the function with different strings and print the results.

def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]

# Example usage
word = input("Enter a word")
if is_palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,' is not a palindrome')
