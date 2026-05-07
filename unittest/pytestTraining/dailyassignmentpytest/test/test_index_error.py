# 3. Handling Exceptions
# Goal:  Use the `pytest.raises` context manager.
# Write a function `get_element(my_list, index)` that returns an item from a list. Write a
# test function `test_index_error` that uses `with pytest.raises(IndexError):` to verify that
# attempting to access index `10` of the list `[1, 2, 3]` correctly triggers an error.

# test_exceptions.py
import pytest

# Function to get element from a list
def get_element(my_list, index):
    return my_list[index]

# Test to verify IndexError is raised
def test_index_error():
    numbers = [1, 2, 3]
    with pytest.raises(IndexError):
        get_element(numbers, 10)
