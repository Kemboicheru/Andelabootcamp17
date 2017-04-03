import sys
import unittest
from loancalculator import CalculateRepayment

class LoanCalculator(unittest.TestCase):
    def test_integer_values_only(self):
        self.assertEquals(CalculateRepayment(100000,12,12), 112000)

    def test_param_time(self):
        self.assertEquals(sys.argv[2],12);


if __name__ == '__main__':
    unittest.main()
