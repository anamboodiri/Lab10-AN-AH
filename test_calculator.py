import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 7), -21)
        self.assertEqual(multiply(0, 99), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-12, 3), -4)
        self.assertEqual(divide(7.5, 2.5), 3.0)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
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
