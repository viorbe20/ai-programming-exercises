"""
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. 
Carga las lista number con valores aleatorios entre 0 y 100. 
En la lista square se deben almacenar los cuadrados de los valores que hay en number. 
En la lista cube se deben almacenar los cubos de los valores que hay en number. 
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.
Usa numpy.
Author: Virginia Ordoño Bernier
Date: november 2023
"""

import numpy as np

number = np.random.randint(0, 101, 20)
square = number**2
cube = number**3

# Array 2d
data = np.vstack((number, square, cube)).T

column_names = ['Number', 'Square', 'Cube']

print("\n")
for column_name in column_names:
    print(column_name, end='\t')
print("\n")


for row in data:
    for value in row:
        print(value, end='\t')
    print("\n")