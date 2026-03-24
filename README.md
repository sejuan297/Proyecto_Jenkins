# Proyecto de Ejercicios Matemáticos

Este proyecto contiene un conjunto de funciones matemáticas básicas y avanzadas implementadas en Python, junto con sus respectivas pruebas unitarias.

## Funcionalidades

### Operaciones Básicas
- **Suma**: Suma de dos números
- **Resta**: Resta de dos números  
- **Multiplicación**: Multiplicación de dos números
- **División**: División de dos números (con manejo de división entre cero)

### Operaciones Avanzadas
- **Potencia**: Calcula la potencia de un número
- **Raíz Cuadrada**: Calcula la raíz cuadrada (con manejo de números negativos)
- **Factorial**: Calcula el factorial de un número
- **Verificación de Primos**: Determina si un número es primo

## Estructura del Proyecto

```
Proyecto_Jenkins/
├── main.py              # Funciones matemáticas principales
├── test_ejercicios.py   # Pruebas unitarias
├── README.md           # Documentación del proyecto
└── requirements.txt    # Dependencias del proyecto
```

## Instalación y Ejecución

### Prerrequisitos
- Python 3.6 o superior

### Ejecutar el programa principal
```bash
python main.py
```

### Ejecutar las pruebas
```bash
python test_ejercicios.py
```

O usando unittest:
```bash
python -m unittest test_ejercicios.py
```

## Ejemplo de Salida

Al ejecutar `main.py`, verás:

```
=== PROYECTO DE EJERCICIOS MATEMÁTICOS ===

Operaciones Básicas:
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0

Operaciones Avanzadas:
2^3 = 8
√16 = 4.0
5! = 120

Verificación de Números Primos:
2 es primo
3 es primo
4 no es primo
5 es primo
7 es primo
8 no es primo
11 es primo
13 es primo
15 no es primo

=== EJERCICIOS COMPLETADOS ===
```

## Pruebas Unitarias

El proyecto incluye pruebas unitarias completas para todas las funciones matemáticas, asegurando que:
- Las operaciones básicas funcionan correctamente
- Se manejan casos especiales (división entre cero, números negativos)
- Las operaciones avanzadas dan resultados precisos
- La verificación de números primos es correcta

## Integración con Jenkins

Este proyecto está diseñado para ser integrado con Jenkins para CI/CD:
- Las pruebas unitarias pueden ejecutarse automáticamente
- El código está estructurado para fácil mantenimiento
- Incluye documentación completa

## Autor

Desarrollado para demostrar integración con Git y Jenkins
