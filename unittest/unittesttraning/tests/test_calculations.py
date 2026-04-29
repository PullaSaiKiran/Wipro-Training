import sys
import unittest
from src.calculations import add,sub,mul,div,ne

class TestCalculation(unittest.TestCase):
    def test_add(self):
        res = add(10,5)
        self.assertEqual(15,res,msg='Addition Error')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual( 5,res, msg='Subtraction Error')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50,res, msg='Multiplication Error')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual( 2.0,res, msg='Division Error')

    def test_ne(self):
        res = ne(10,10)
        self.assertTrue(res, msg='NE')

    @unittest.skip("Skipping division by zero test")
    def test_div_zero(self):
        # This test will be skipped
        res = div(10, 0)
        self.assertEqual(2.0, res, msg='Division Error')