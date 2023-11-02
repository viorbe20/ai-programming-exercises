"""
Escribe un programa que genere 20 números enteros entre 100 y 999. 
Estos números se deben introducir en una lista de 4 filas por 5 columnas. 
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. 
La suma total debe aparecer en la esquina inferior derecha.
Author: Virginia Ordoño Bernier
Date: november 2023
"""
import random

random_numbers = [random.randint(100, 999) for _ in range(20)]

ROWS = 4
COLUMNS = 5
numbers_list = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)] # Initializes with 0

print("\n")
for i in range(ROWS):
    for j in range(COLUMNS):
        numbers_list[i][j] = random_numbers[i * COLUMNS + j] # Overwrites 0 with a random number from the list
        print(numbers_list[i][j], end="\t")
    print("\n")