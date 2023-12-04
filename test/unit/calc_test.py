import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(1, self.calc.power(1, 10))
        self.assertEqual(100, self.calc.power(10, 2))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(8, self.calc.power(2, 3))

    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.raiz_cuadrada(4))
        self.assertEqual(3, self.calc.raiz_cuadrada(9))
        self.assertEqual(0, self.calc.raiz_cuadrada(0))
        
    def test_square_root_method_fails_with_negative_number(self):
        self.assertRaises(ValueError, self.calc.raiz_cuadrada, -4)

    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.logaritmo_base_10(1))
        self.assertEqual(1, self.calc.logaritmo_base_10(10))
        self.assertEqual(2, self.calc.logaritmo_base_10(100))

    def test_logarithm_method_fails_with_non_positive_number(self):
        self.assertRaises(ValueError, self.calc.logaritmo_base_10, 0)
        self.assertRaises(ValueError, self.calc.logaritmo_base_10, -10)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
