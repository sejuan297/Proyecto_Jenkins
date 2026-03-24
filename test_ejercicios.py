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
    
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 2), 25)
        self.assertEqual(potencia(3, 0), 1)
    
    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(9), 3)
        self.assertEqual(raiz_cuadrada(16), 4)
        self.assertEqual(raiz_cuadrada(-4), "Error: No se puede calcular raíz cuadrada de número negativo")
    
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(-1), "Error: No se puede calcular factorial de número negativo")
    
    def test_es_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(11))
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(9))

if __name__ == '__main__':
    unittest.main()
