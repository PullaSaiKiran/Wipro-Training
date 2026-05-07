# 1. The Basic Assertion
# Goal:  Understand the simplicity of pytest syntax.
# Write a file named `test_logic.py`. Create a test function `test_math_operations` that
# uses simple `assert` statements to verify:
# That $15 \times 3$ equals $45$.
# That the string `"pytest"` is present within the phrase `"Learning pytest is fun"`

# test_logic.py

def test_math_operations():
    # Check multiplication
    assert 15 * 3 == 45

    # Check substring presence
    assert "pytest" in "Learning pytest is fun"
