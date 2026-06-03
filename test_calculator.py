"""Unit-тесты для модуля calculator."""

import unittest

from calculator import add, divide, is_even, multiply, subtract


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)


class TestSubtract(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)


class TestMultiply(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_by_zero(self):
        self.assertEqual(multiply(100, 0), 0)


class TestDivide(unittest.TestCase):
    def test_basic(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))

    def test_odd(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))


if __name__ == "__main__":
    unittest.main()
