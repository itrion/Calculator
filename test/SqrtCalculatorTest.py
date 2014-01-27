import unittest
from calculator import NegativeSqrtError
from calculator.Calculator import *


class SqrtCalculatorTest (unittest.TestCase):

	def test_sqrt(self):
		calculator = Calculator()
		self.assertEquals(5, calculator.sqrt(25))
		self.assertEquals(6, calculator.sqrt(36))
		self.assertEquals(0, calculator.sqrt(0))

	def test_sqrt_negative(self):
		calculator = Calculator()
		self.assertRaises(NegativeSqrtError, calculator.sqrt, -1)

if __name__ == '__main__':
	unittest.main()