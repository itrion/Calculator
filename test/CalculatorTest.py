import unittest
from calculator.Calculator import *

class CalculatorTest (unittest.TestCase):

	def test_Sum(self):
		calculator = Calculator()
		self.assertEquals(4, calculator.sum(2, 2))
		self.assertEquals(6, calculator.sum(calculator.sum(2, 2), 2))
		self.assertEquals(8, calculator.sum(calculator.sum(2, 2), calculator.sum(2, 2)))

	def test_Substract(self):
		calculator = Calculator()
		self.assertEquals(0, calculator.substract(2, 2))
		self.assertEquals(-2, calculator.substract(calculator.substract(2, 2), 2))
		self.assertEquals(0, calculator.substract(calculator.substract(2, 2), calculator.substract(2, 2)))

if __name__ == '__main__':
	unittest.main()