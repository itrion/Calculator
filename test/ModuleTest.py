__author__ = 'Soulkyiro'

import unittest
from calculator.Calculator import *


class ModuleTest(unittest.TestCase):
    def test_module(self):
        calculator = Calculator()
        self.assertEquals(1, calculator.mod(16, 3))
        self.assertEquals(2, calculator.mod(17, 3))
        self.assertEquals(3, calculator.mod(23, 4))
        self.assertEquals(0, calculator.mod(4, 2))


def test_module_zero(self):
    calculator = Calculator()
    try:
        self.assertRaises(ZeroDivisionError, calculator.mod(4, 0))
    except ZeroDivisionError:
        pass


if __name__ == '__main__':
    unittest.main()
