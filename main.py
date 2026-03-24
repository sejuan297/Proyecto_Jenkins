#!/usr/bin/env python3
"""
Proyecto de Ejercicios Matemáticos
Este proyecto contiene funciones para realizar operaciones matemáticas básicas
"""

def suma(a, b):
    """Realiza la suma de dos números"""
    return a + b

def resta(a, b):
    """Realiza la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Realiza la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Realiza la división de dos números"""
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(base, exponente):
    """Calcula la potencia de un número"""
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número"""
    if numero < 0:
        return "Error: No se puede calcular raíz cuadrada de número negativo"
    return numero ** 0.5

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return "Error: No se puede calcular factorial de número negativo"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def es_primo(numero):
    """Verifica si un número es primo"""
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def main():
    """Función principal que ejecuta ejemplos de las operaciones matemáticas"""
    print("=== PROYECTO DE EJERCICIOS MATEMÁTICOS ===")
    print()
    
    # Ejemplos de operaciones básicas
    print("Operaciones Básicas:")
    print(f"10 + 5 = {suma(10, 5)}")
    print(f"10 - 5 = {resta(10, 5)}")
    print(f"10 * 5 = {multiplicacion(10, 5)}")
    print(f"10 / 5 = {division(10, 5)}")
    print()
    
    # Ejemplos de operaciones avanzadas
    print("Operaciones Avanzadas:")
    print(f"2^3 = {potencia(2, 3)}")
    print(f"Raiz cuadrada de 16 = {raiz_cuadrada(16)}")
    print(f"5! = {factorial(5)}")
    print()
    
    # Ejemplos de verificación de primos
    print("Verificación de Números Primos:")
    numeros_prueba = [2, 3, 4, 5, 7, 8, 11, 13, 15]
    for num in numeros_prueba:
        print(f"{num} {'es primo' if es_primo(num) else 'no es primo'}")
    
    print()
    print("=== EJERCICIOS COMPLETADOS ===")

if __name__ == "__main__":
    main()
