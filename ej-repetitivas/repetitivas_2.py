"""
Crea una aplicación que permita adivinar un número. 
La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
si se llega al limite de intentos te muestra el número que había generado.
Para usar números aleatorios en Python: http://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html
Date: october 2023.
Author: Virginia Ordoño Bernier

No me he dado cuenta que había un límtie de 10 intentos.
"""

import random

print("\nA continuación, debes adivinar el número que estoy pensando entre el 1 y el 100. Introduce números y el te diré si es mayor o menor.")

attempts = 0
number = random.randint(1, 101)

while True:
    try:
        number_user = int(input("\nIntroduce un número: "))
        attempts += 1

        if number_user > number:
            print("El número que has introducido es mayor que el número que estoy pensando.")
        elif number_user < number:
            print("El número que has introducido es menor que el número que estoy pensando.")
        else:
            print(f"\n¡Enhorabuena! Has acertado el número que estoy pensando en {attempts} intentos.\n")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")



