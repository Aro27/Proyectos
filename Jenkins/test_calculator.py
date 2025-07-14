import unittest
from calculadora import multiplicar

class TestCalculadora(unittest.TestCase):
    def test_multiplicacion_positivos(self):
        """Test multiplicación de números positivos"""
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(1.5, 2), 3.0)

    def test_multiplicacion_negativos(self):
        """Test multiplicación con números negativos"""
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(-2, -3), 6)

    def test_multiplicacion_strings(self):
        """Test multiplicación con strings numéricos"""
        self.assertEqual(multiplicar("2", "3"), 6)
        self.assertEqual(multiplicar("1.5", "2"), 3.0)

    def test_multiplicacion_strings_no_numericos(self):
        """Test multiplicación con strings no numéricos"""
        self.assertRaises(ValueError, multiplicar, "a", "b")

if __name__ == '__main__':
    unittest.main() 