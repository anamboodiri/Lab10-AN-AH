#https://github.com/anamboodiri/Lab10-AN-AH
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(9, 10), 19)
        self.assertEqual(add(18, 9), 27)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(9, 10), -1)
        self.assertEqual(subtract(14, 8), 6)
    #     fill in code
    ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-3, 7), -21)
        self.assertEqual(mul(0, 99), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, -12), -4)
        self.assertEqual(div(2.5, 7.5), 3.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(15, 0), 0)
        self.assertEqual(div(90, 0), 0)
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(9, 81), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            self.assertEqual(logarithm(3, -90), 0)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)  # log(0) is undefined

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(1.2, 3.4), (1.2**2 + 3.4**2)**0.5)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-9)  # can't sqrt a negative number
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
