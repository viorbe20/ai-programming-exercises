"""
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
Si introducimos otro número nos da un error.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""

print("\nA continuación, el programa determinará el día de la semana según el número")

try:
    
    day_number = int(input("\nIntroduce el número del día de la semana: "))

    if day_number == 1:
        print("\nEl día de la semana es lunes")
    elif day_number == 2:
        print("\nEl día de la semana es martes")
    elif day_number == 3:
        print("\nEl día de la semana es miércoles")
    elif day_number == 4:
        print("\nEl día de la semana es jueves")
    elif day_number == 5:
        print("\nEl día de la semana es viernes")
    elif day_number == 6:
        print("\nEl día de la semana es sábado")
    elif day_number == 7:
        print("\nEl día de la semana es domingo")
    else:
        print("\nError: debes introducir un número del 1 al 7. Inténtalo de nuevo.")
except ValueError:
    print("\nValor incorrecto. Inténtalo de nuevo.")
    exit()


