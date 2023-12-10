"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar qué tipo de triangulo es, teniendo en cuenta los siguiente:
Si se cumple Pitágoras entonces es triángulo rectángulo 
Si sólo dos lados del triángulo son iguales entonces es isósceles (dos lados iguales).
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
Date: october 2023.
Author: Virginia Ordoño Bernier
Rectángulo: el cuadrado de la longitud de la hipotenusa es igual a la suma de los cuadrados de los catetos.
"""

print("\nA continuación el programa te pedirá que introduzcas las dimensiones de un triángulo \npara determinar qué tipo de triángulo es.")

try:
    side1 = float(input("\nIntroduce la dimensión del lado 1: "))
    side2 = float(input("\nIntroduce la dimensión del lado 2: "))
    side3 = float(input("\nIntroduce la dimensión del lado 3: "))
except ValueError:
    print("\nEl valor introducido no es válido.")
    exit(1)

# Check triangle's type
if side1 == side2 == side3:
    print("\nEl triángulo es equilátero.")
else:
    if side1 == side2 or side2 == side3 or side1 == side3:
        print("\nEl triángulo es isósceles.")
    else:
        print("\nEl triángulo es escaleno.")
    
    if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
        print("\nEl triángulo es rectángulo.")