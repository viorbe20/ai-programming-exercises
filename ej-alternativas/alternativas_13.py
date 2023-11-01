"""
Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al primero. 
Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más cercano al 2 es el 1.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, ingresa cinco números, el programa determinará cuál de los cuatro últimos números es más cercano al primero.")

numbers = []

try:
    main_number = int(input("Introduce el primer número entero: "))
    num1 = int(input("Introduce el segundo número entero: "))
    num2 = int(input("Introduce el tercer número entero: "))
    num3 = int(input("Introduce el cuarto número entero: "))
    num4 = int(input("Introduce el quinto número entero: "))
except ValueError:
    print("\nValor incorrecto. Inténtalo de nuevo.\n")
    exit(1)

# Create a list with the numbers

numbers.extend([num1, num2, num3, num4])

# Establish position 0 as the closest number 

min_distance = abs(main_number - numbers[0])
closest_number = numbers[0]

# Iterate and compare the distance to the main number

for n in numbers[1:]:
    n_distance = abs(main_number - n)
    if n_distance < min_distance:
        min_distance = n_distance
        closest_number = n

print(f"\nEl número más cercano al {main_number} es el {closest_number}.\n")