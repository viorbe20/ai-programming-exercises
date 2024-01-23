"""
V1
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: 
sumar, restar, multiplicar, dividir y terminar. 
- Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. 
- Si se introduce una opción incorrecta se muestra un mensaje de error. 
- El menú se volverá a mostrar, a menos que no se de a la opción terminar.

V2
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). 
- Las variables se inicializan a cero. Si no se introduce nada, hace las operaciones a 0.

V3
Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente 
no se puedan ejecutar el resto de las opciones. a y b no se inicializan a cero.

V4
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, 
pide una opción (por su número) y devuelve la opción escogida. 
Modifica el último programa para que use esta función. 

Author: Virginia Ordoño Bernier
Date: november 2023
"""

def menu_management(*args):
    
    for option in range(len(args)):
        print(f"{option+1}. {args[option]}")
    
    
    option = int(input("Elige una opción: "))
    if option > len(args):
        return print("Opción no válida")
    else:
        return args[option-1]


print(menu_management('Opción 1','Opción 2','Opción 3'))