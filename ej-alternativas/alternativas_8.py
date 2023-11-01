"""
El director de una escuela está organizando un viaje de estudios, 
y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. 
La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, 
de 30 a 49, de 95 euros, y si son menos de 30, 
el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa determinará el pago a la compañía de autobuses y lo que se debe pagar por cada alumno.")

try:
    students_num = int(input("Introduce el número de alumnos que realizarán el viaje: "))
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit(1)

if students_num >= 100:
    students_cost = 65
    bus_cost = 4000
    print(f"\nEl costo por cada alumno es de {students_cost} euros.")
    print(f"El costo de la renta del autobús es de {bus_cost} euros.")
    print(f"El pago a la compañía de autobuses es de {students_cost * students_num} euros.")
elif students_num >= 50 and students_num <= 99:
    students_cost = 70
    bus_cost = 4000
    print(f"\nEl costo por cada alumno es de {students_cost} euros.")
    print(f"El costo de la renta del autobús es de {bus_cost} euros.")
    print(f"El pago a la compañía de autobuses es de {students_cost * students_num} euros.")
elif students_num >= 30 and students_num <= 49:
    students_cost = 95
    bus_cost = 4000
    print(f"\nEl costo por cada alumno es de {students_cost} euros.")
    print(f"El costo de la renta del autobús es de {bus_cost} euros.")
    print(f"El pago a la compañía de autobuses es de {students_cost * students_num} euros.")
elif students_num < 30 and students_num >= 0:
    students_cost = 0
    bus_cost = 4000
    print(f"\nEl costo por cada alumno es de {students_cost} euros.")
    print(f"El costo de la renta del autobús es de {bus_cost} euros.")
    print(f"El pago a la compañía de autobuses es de {students_cost} euros.")
else:
    print("\nEl valor introducido no es válido.")