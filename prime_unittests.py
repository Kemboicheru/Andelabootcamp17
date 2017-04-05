import sys
import unittest
from primenumbers import generate_prime_numbers

class Prime_numbers(unittest.TestCase):
    def test_zero(self):
        self.assertEquals(generate_prime_numbers(0), [])

    def test_two(self):
        self.assertEquals(generate_prime_numbers(2), [2]);

    def test_more_three(self):
        self.assertEquals(generate_prime_numbers(3), [2,3]);
    


if __name__ == '__main__':
    unittest.main()
