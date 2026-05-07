# 2. Using Fixtures for Setup
# Goal:  Replace `setUp` and `tearDown` with the modern `@pytest.fixture` approach.
# Create a pytest fixture named `sample_dict` that returns a dictionary: `{"name":
# "Alice", "role": "Dev"}`.
# Write a test function `test_dict_keys` that:
# Accepts the fixture as an argument.
# Asserts that the key `"role"` exists in the dictionary.
# Asserts that the value of `"name"` is `"Alice"`.


# test_fixture_dict.py
import pytest


@pytest.fixture
def sample_dict():
    print("\nSetup: Creating dictionary")
    data = {"name": "Alice", "role": "Dev"}
    yield data
    print("Teardown: Dictionary test completed")

# Use the fixture in a test
def test_dict_keys(sample_dict):

    assert "role" in sample_dict


    assert sample_dict["name"] == "Alice"
