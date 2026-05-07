# 5. Cleaning Up with Fixture Yields
# Goal:  Manage resources (like files or database connections) properly.
# Create a fixture named `temp_file`.
# In the  Setup phase : Create a new text file named `test.txt` and write `"Hello World"`
# into it.
# Yield  the filename to the test.
# In the  Teardown phase  (after the yield): Use the `os` module to delete the file.
# Write a test `test_file_content` that reads the file and verifies the text matches.


# test_temp_file.py
import pytest
import os

# Fixture to create and clean up a temporary file
@pytest.fixture
def temp_file():
    # Setup phase: create file and write content
    filename = "test.txt"
    with open(filename, "w") as f:
        f.write("Hello World")
    print("\nSetup: File created")

    # Yield the filename to the test
    yield filename

    # Teardown phase: delete file
    if os.path.exists(filename):
        os.remove(filename)
        print("Teardown: File deleted")

# Test that uses the fixture
def test_file_content(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "Hello World"
