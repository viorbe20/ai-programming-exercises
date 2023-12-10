"""
Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación debes introducir dos números para que el programa te diga si el primero es mayor que el segundo o no.\n")

# Ask and check number 1
try:
    n1 = float(input("\nIntroduce el primer número: "))
except ValueError:
    print("\nEl valor introducido no es un número válido.")
    exit(1)

# Ask and check number 2
try:
    n2 = float(input("\nIntroduce el segundo número: "))
except ValueError:
    print("\nEl valor introducido no es un número válido.")
    exit(1)

# Result
if n1 == n2:
    print("\nLos números son iguales.") 
elif n1 > n2:
    print("\nEl primer número es mayor que el segundo.")
else:
    print("\nEl segundo número es mayor que el primero.")