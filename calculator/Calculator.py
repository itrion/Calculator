class Calculator:
    def __init__(self):
        pass

    def substract(self, number_a, number_b):
        return number_a - number_b

    def sum(self, number_a, number_b):
        return number_a + number_b

    def pow(self, base, exponent):
        result = 1

        for i in range(exponent):
            result = result * base

        return result