import unittest
from calculator.Calculator import Calculator


class DivisionCalculatorTest(unittest.TestCase):
    def test_Division(self):
        calculator = Calculator()
        self.assertEqual(2, calculator.div(4, 2))
        self.assertEqual(0.5, calculator.div(1, 2))
        self.assertEqual(2, calculator.div(2, 1))

if __name__ == '__main__':
    unittest.main()
