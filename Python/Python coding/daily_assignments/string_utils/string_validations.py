# string_validations.py

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # normalize
    return s == s[::-1]

def is_alpha(s):
    return s.isalpha()
