"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

even_numbers = []

print("\nA continuación, debes introducir dos números para que el programa te muestre todos los números pares que hay entre los dos.\n")

while True:
    try:
        num1 = int(input("\nIntroduce el primer número: "))
        num2 = int(input("\nIntroduce el segundo número: "))
        break  
    except ValueError:
        print("\nIntroduce un número válido.")

# If num1 is bigger than num2, it swaps them
if num1 > num2:
    num1, num2 = num2, num1

print(f"\nLos números pares entre {num1} y {num2} son: ")

# Iterate and show even numbers
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        even_numbers.append(i)

# Show result
if len(even_numbers) == 0:
    print("\nNo hay números pares entre los dos números introducidos.\n")
else:
    print(even_numbers)