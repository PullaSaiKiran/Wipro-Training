import unittest
from unittesttraning.dailyassignmentunittest.src.BasicUnit import add

class TestCalcu(unittest.TestCase):
    def test_add(self):
        res = add(10,5)
        self.assertEqual(15,res,msg='Addition Error')

    def setUp(self):
        self.my_list = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(len(self.my_list), 3, "Expected list length to be 3")

    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0

    def test_divide_by_zero_message(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            10 / 0
        self.assertIn("division by zero", str(cm.exception))



# First test class
class TestAdd(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5, "Expected 2 + 3 to equal 5")

# Second test class
class TestSubtract(unittest.TestCase):
    def test_subtraction(self):
        result = 10 - 4
        self.assertEqual(result, 6, "Expected 10 - 4 to equal 6")

# Combine into a suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))
    return suite
