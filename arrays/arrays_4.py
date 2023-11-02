"""
Escribe un programa que lea 5 números por teclado y que los almacene en una lista. 
Rota los elementos de esa lista, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. 
El número que se encuentra en la última posición debe pasar a la posición 0. 
Finalmente, muestra el contenido de la lista.
Author: Virginia Ordoño Bernier
Date: november 2023
"""

import numpy as np

numbers_list = np.empty(5, dtype=int)

print("\nIntroduce 5 números por teclado. El programa desplazará el último elemento a la primera posición, el primero a la segunda posición y así sucesivamente.")

while True:
    try:
        numbers_list[0] = int(input("\nIntroduce el primer número: "))
        numbers_list[1] = int(input("\nIntroduce el segundo número: "))
        numbers_list[2] = int(input("\nIntroduce el tercer número: "))
        numbers_list[3] = int(input("\nIntroduce el cuarto número: "))
        numbers_list[4] = int(input("\nIntroduce el quinto número: "))

        numbers_list = np.roll(numbers_list, 1)  # Rotation of the elements of the array, 1 position 

        if all(numbers_list != 0):
            break
    except ValueError:
        print("Los números deben ser enteros.")

print("\nLa lista después de desplazarse es la siguiente:")

for i in numbers_list:
    print(i, end=" ")