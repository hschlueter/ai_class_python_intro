import unittest
from fib import fibbonacci


class TestFibbonacci(unittest.TestCase):
    def test_definition(self):
        self.assertEqual(fibbonacci(1), 1)
        self.assertEqual(fibbonacci(2), 1)

    def test_calculated_values(self):
        self.assertEqual(fibbonacci(5), 5)
        self.assertEqual(fibbonacci(6), 8)


if __name__ == '__main__':
    unittest.main()
