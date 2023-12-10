"""
Escribe un programa que lea un número e indique si es par o impar.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación debes introducir un número para que el programa te diga si es par o impar.\n")

n = input("\nIntroduce el número: ")

try:
    n = float(n)
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit()

if n % 2 == 0:
    print("\nEl número es par.")
else:
    print("\nEl número es impar.")