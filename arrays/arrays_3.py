"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. 
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) 
y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
Author: Virginia Ordoño Bernier
Date: november 2023
"""

import numpy as np

random_numbers = np.random.randint(0, 100, 20)

for n in random_numbers:
    if n % 2 == 0:
        random_numbers = np.delete(random_numbers, np.where(random_numbers == n)) # Deletes the number
        random_numbers = np.insert(random_numbers, 0, n) # Inserte the number at the beginning of the array


print(random_numbers)