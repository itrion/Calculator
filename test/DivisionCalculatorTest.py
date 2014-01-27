import unittest
from calculator.Calculator import Calculator


class DivisionCalculatorTest(unittest.TestCase):
    def test_Division(self):
        calculator = Calculator()
        self.assertEqual(2, calculator.div(4, 2))
        self.assertEqual(0, calculator.div(1, 2))
        self.assertEqual(2, calculator.div(2, 1))

    def test_DivisionBy0(self):
        calculator = Calculator()
        try:
            self.assertRaises(ZeroDivisionError, calculator.div(5, 0))
        except ZeroDivisionError:
            pass


if __name__ == '__main__':
    unittest.main()
