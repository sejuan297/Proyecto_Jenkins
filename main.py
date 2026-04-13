#!/usr/bin/env python3
"""
Proyecto de Ejercicios Matemáticos
Este proyecto contiene funciones para realizar operaciones matemáticas básicas
NUEVA ACTUALIZACIÓN
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def obtener_numero(mensaje):
    #Función para obtener un número válido del usuario
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingrese un número válido")

def main():
    #Función principal que permite al usuario realizar operaciones matemáticas
    print("=== CALCULADORA MATEMÁTICA ===")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print()
    
    while True:
        try:
            opcion = int(input("Seleccione una operación (1-5): "))
            
            if opcion == 5:
                print("¡Gracias por usar la calculadora!")
                break
                
            if opcion not in [1, 2, 3, 4]:
                print("Opción no válida. Intente nuevamente.")
                continue
                
            num1 = obtener_numero("Ingrese el primer número: ")
            num2 = obtener_numero("Ingrese el segundo número: ")
            
            if opcion == 1:
                resultado = suma(num1, num2)
                if resultado.is_integer():
                    print(f"Resultado: {int(num1)} + {int(num2)} = {int(resultado)}")
                else:
                    print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == 2:
                resultado = resta(num1, num2)
                if resultado.is_integer():
                    print(f"Resultado: {int(num1)} - {int(num2)} = {int(resultado)}")
                else:
                    print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == 3:
                resultado = multiplicacion(num1, num2)
                if resultado.is_integer():
                    print(f"Resultado: {int(num1)} * {int(num2)} = {int(resultado)}")
                else:
                    print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == 4:
                resultado = division(num1, num2)
                if resultado.is_integer():
                    print(f"Resultado: {int(num1)} / {int(num2)} = {int(resultado)}")
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                
            print()
            
        except ValueError:
            print("Error: Por favor ingrese una opción válida (1-5)")
            print()

if __name__ == "__main__":
    main()
