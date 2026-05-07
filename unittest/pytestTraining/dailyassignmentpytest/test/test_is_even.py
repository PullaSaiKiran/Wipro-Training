#
# #4.Parameterized Testing
# Goal:  Run the same test logic with multiple sets of data.
# Use the `@pytest.mark.parametrize` decorator to create a single test function
# `test_is_even`.
# Pass three different inputs to the test: `2`, `10`, and `22`.
# The test should assert that each input `% 2 == 0`.
# Observe how pytest treats these as three separate test cases in the output.
# # test_parametrize_even.py
import pytest

# Parameterized test
@pytest.mark.parametrize("number", [2, 10, 22])
def test_is_even(number):
    assert number % 2 == 0
