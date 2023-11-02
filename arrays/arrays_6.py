"""
Escribe un programa que genere 20 números enteros entre 100 y 999. 
Estos números se deben introducir en una lista de 4 filas por 5 columnas. 
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. 
La suma total debe aparecer en la esquina inferior derecha.
Usa numpy
Author: Virginia Ordoño Bernier
Date: november 2023
"""
import numpy as np
import random

ROWS = 4
COLUMNS = 5

random_numbers = [random.randint(100, 999) for _ in range(20)]

# Tranforms array into a matrix of 4 rows and 5 columns
numbers_list = np.array(random_numbers).reshape(ROWS, COLUMNS)

print(numbers_list)