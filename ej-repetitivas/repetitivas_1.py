"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

import random

print("\nA continuación, el programa te pedirá que introduzcas una cantidad de números y calculará cuantos son mayores que 0, menores que 0 e iguales a 0.")

amount = random.randint(1, 5)
numbers = []


# Ask for amount of numbers
for _ in range(amount):
    number = None
    
    while number is None:
        try:
            print(f"\nDebes introducir {amount} números. Te quedan {amount - len(numbers)}.")
            number = int(input("Introduce un número: "))
        except ValueError:
            print("\nEl valor introducido no es un número entero válido. Vuelve a intentarlo.")

    numbers.append(number)

# Calcute how many numbers are greater than 0, less than 0 and equal to 0.
gt_0 = 0
lt_0 = 0
eqt_0 = 0

for number in numbers:
    if number > 0:
        gt_0 += 1
    elif number < 0:
        lt_0 += 1
    else:
        eqt_0 += 1

# Result
print(f"\nLa cantidad de números introducidos es: {amount}.")
print(f"--------------------------------------------")
print(f"Números mayores que 0 => {gt_0}.")
print(f"Números menores que 0 => {lt_0}.")
print(f"Números iguales a 0 => {eqt_0}.\n")