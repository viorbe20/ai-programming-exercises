"""
Escribir un programa que lea un año e indicar si es bisiesto 
(un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
excepto que también sea divisible por 400).
Date: october 2023.
Author: Virginia Ordoño Bernier
Sobre la regex:
- Pueden comenzar opcionalmente con un signo negativo (-).
- Entre 1 y 4 dígitos consecutivos.
- La cadena no debe contener ningún otro carácter antes o después de los dígitos.
Sin r '^-?\\d{1,4}$'. Con ella evitas duplicar barras invertidas
"""
import re 

YEAR_REGEX = r'^-?\d{1,4}$'

print("\nA continuación, el programa te pedirá que introduzcas un año para determinar si es bisiesto o no.")

# Ask for a year
year_input = input("\nIntroduce un año: ")

# Check input with regex
if not re.match(YEAR_REGEX, year_input):
    print("\nEl valor introducido no es un año válido.")
else:
    year = int(year_input)

    # Check if is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("\nEl año es bisiesto.")
    else:
        print("\nEl año no es bisiesto.")

    exit()
        






































