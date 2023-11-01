"""
Realiza un programa que pida tres números enteros y diga cuál es el mayor.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa te pedirá tres números enteros y te dirá cuál es el mayor")

try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    num3 = int(input("Introduce el tercer número entero: "))
except ValueError:
    print("\nValor incorrecto. Inténtalo de nuevo.\n")
    exit(1)

largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"\nEl número mayor es: {largest}\n")