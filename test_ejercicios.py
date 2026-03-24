#!/usr/bin/env python3
"""
Tests unitarios para los ejercicios matemáticos
"""

import unittest
from main import *

class TestEjerciciosMatematicos(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(-2, 7), 5)
        self.assertEqual(suma(0, 0), 0)
    
    def test_resta(self):
        self.assertEqual(resta(10, 4), 6)
        self.assertEqual(resta(5, 8), -3)
        self.assertEqual(resta(0, 0), 0)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 5), 20)
        self.assertEqual(multiplicacion(-3, 6), -18)
        self.assertEqual(multiplicacion(0, 10), 0)
    
    def test_division(self):
        self.assertEqual(division(15, 3), 5)
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(10, 0), "Error: No se puede dividir entre cero")

if __name__ == '__main__':
    unittest.main()
