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

for i in range(len(number)):
    print(f"{number[i]:5} {square[i]:5} {cube[1]:5}")