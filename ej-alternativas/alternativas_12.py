"""
Realiza un programa que pida cinco números enteros y diga cuál es el mayor.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa te pedirá cinco números enteros y te dirá cuál es el mayor")

try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    num3 = int(input("Introduce el tercer número entero: "))
    num4 = int(input("Introduce el cuarto número entero: "))
    num5 = int(input("Introduce el quinto número entero: "))
except ValueError:
    print("\nValor incorrecto. Inténtalo de nuevo.\n")
    exit()

largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
if num5 > largest:
    largest = num5

print(f"\nEl número mayor es: {largest}\n")