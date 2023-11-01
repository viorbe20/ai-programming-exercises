"""
Realizar un programa que compruebe si una cadena contiene una subcadena. 
Las dos cadenas se introducen por teclado. No se pueden usar los métodos de Python para este fin ni slices.
Date: october 2023.
Author: Virginia Ordoño Bernier
"""
print("\nA continuación, el programa te indicará si una cadena contiene una subcadena.")

string = input("\nIntroduce  la cadena: ")
substring = input("Introduce la subcadena: ")


if substring in string:
    print("\nLa cadena contiene la subcadena.")
    
else:
    print("\nLa cadena no contiene la subcadena.")