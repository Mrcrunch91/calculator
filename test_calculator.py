import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        nums = [1,2,3,4,5]
        self.assertEqual(multiplyAllNumbers(nums), 10)

