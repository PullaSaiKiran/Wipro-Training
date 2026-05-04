#
# Basic Test Case
# Write a unittest class TestMath with one test method that checks if 2 + 3 equals 5.
# Setup and Teardown
# Create a test class that uses setUp() to initialize a list [1, 2, 3] and tearDown() to print
# "Test completed".
# Verify that the list length is 3 inside your test method.
# Multiple Assertions
# Write a test class TestStringMethods with methods to test:
# "hello".upper() equals "HELLO"
# "hello".isupper() returns False
# Exception Testing
# Use assertRaises to verify that dividing by zero (10 / 0) raises a ZeroDivisionError.
# Test Suite Execution
# Create two test classes (TestAdd and TestSubtract) and combine them into a single test
# suite using unittest.TestSuite.
# Run the suite using unittest.TextTestRunner().


def add(n1,n2):
    return n1+n2