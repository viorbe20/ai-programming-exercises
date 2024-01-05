"""
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. 
Carga las lista number con valores aleatorios entre 0 y 100. 
En la lista square se deben almacenar los cuadrados de los valores que hay en number. 
En la lista cube se deben almacenar los cubos de los valores que hay en number. 
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.
Author: Virginia Ordoño Bernier
Date: november 2023
"""
import random

number = [random.randint(0, 100) for _ in range(20)]
square = [n**2 for n in number]
cube = [n**3 for n in number]

# Array 2 dimensions. One array contains the 3 arrays of numbers
data = [number, square, cube]

# zip(*data) == indexes into a tupla. i.e. (number[0], square[0], cube[0])(number[1], square[1], cube[1]) etc
# list(map(list, ...)): tranforms hte last tuple into a list 
data = list(map(list, zip(*data))) 

print("\n")
column_names = ['Number', 'Square', 'Cube']

# Print names
for column_name in column_names:
    print(column_name, end='\t')
print("\n")

# Print data
for row in data:
    for value in row:
        print(value, end='\t')
    print("\n")