import unittest
from calculator.Calculator import *


class CalculatorTest (unittest.TestCase):

	def test_Sum(self):
		calculator = Calculator()
		self.assertEquals(6, calculator.mul(3, 2))
		self.assertEquals(-12, calculator.mul(calculator.mul(3, 2), -2))
		self.assertEquals(0, calculator.mul(calculator.mul(2, 2), calculator.mul(2, 0)))

if __name__ == '__main__':
	unittest.main()